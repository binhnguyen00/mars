import os

from flask import (Flask, request, jsonify, send_from_directory)
from src.app.context import (ROOT_DIR, UPLOAD_FOLDER, RESULT_FOLDER)

server = Flask(__name__)

@server.route('/', methods=['GET'])
def welcome():
  print(ROOT_DIR)
  file_path = os.path.join(ROOT_DIR, 'ui/public')
  return send_from_directory(directory=file_path, path='index.html')

@server.route('/upload-image', methods=['POST'])
def upload_image():
  if 'image' not in request.files:
    return jsonify({
      'error': 'No image part in the request'
    }), 400

  file = request.files['image']
  if file.filename == '' or not file.filename:
    return jsonify({
      'error': 'No selected file'
    }), 400
  else:
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

  return jsonify({
    'message': 'Image uploaded successfully', 
    'file_path': file_path
  }), 200

def run(debug=True, host='0.0.0.0', port=5000):
  server.run(debug=debug, host=host, port=port)