import os

from flask import Flask, request, jsonify, send_from_directory
from src.module.server.config import (RESULT_FOLDER, UPLOAD_FOLDER)

server = Flask(__name__)
server.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
server.config['RESULT_FOLDER'] = RESULT_FOLDER

@server.route('/', methods=['GET'])
def welcome():
  base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))  # Get the 'src' directory
  file_path = os.path.join(base_dir, 'ui/public')
  return send_from_directory(directory=file_path, path='index.html')

@server.route('/upload-image', methods=['POST'])
def upload_image():
  if 'image' not in request.files:
    return jsonify({'error': 'No image part in the request'}), 400

  file = request.files['image']
  
  if file.filename == '':
    return jsonify({'error': 'No selected file'}), 400

  # Save the file in the 'uploads' directory
  file_path = os.path.join(server.config['UPLOAD_FOLDER'], file.filename)
  file.save(file_path)

  return jsonify({'message': 'Image uploaded successfully', 'file_path': file_path}), 200

def run(debug=True, host='0.0.0.0', port=5000):
  server.run(debug=debug, host=host, port=port)