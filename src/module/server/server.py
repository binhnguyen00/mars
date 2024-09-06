import os
import src.module.image.processor as ImgProcessor

from flask import (Flask, request, jsonify, send_from_directory, send_file)
from flask_cors import CORS
from src.app.context import (ROOT_DIR, UPLOAD_FOLDER, RESULT_FOLDER)

server = Flask(__name__)
CORS(server)

@server.route('/', methods=['GET'])
def welcome():
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
    result_image = ImgProcessor.process_image(file_path, 'png') # png can be replace
    response = send_file(result_image, as_attachment=True)
    return response


@server.route('/get-image/<image_name>', methods=['GET'])
def get_image(image_name):
  directory = os.path.join(RESULT_FOLDER, image_name)
  print(directory)
  return send_file(directory, as_attachment=True)

def run(debug=True, host='0.0.0.0', port=5000):
  server.run(debug=debug, host=host, port=port)