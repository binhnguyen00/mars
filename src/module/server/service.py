import os;
import src.module.image.processor as ImgProcessor;

from flask import (Request, jsonify, send_file);
from src.app.context import (UPLOAD_FOLDER, RESULT_FOLDER);
from src.module.server.controlller import server;
from src.module.database.db import db;

def upload_image(request: Request):
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
    format = request.form.get('format') or 'PNG'
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)
    result_image = ImgProcessor.process_image(file_path, format)
    response = send_file(result_image, as_attachment=True)
    return response

def get_image(image_name):
  directory = os.path.join(RESULT_FOLDER, image_name)
  print(directory)
  return send_file(directory, as_attachment=True)

def run_server(debug=False, host='0.0.0.0', port=5000):
  ImgProcessor.create_result_folder()
  ImgProcessor.create_storing_folder()
  with server.app_context():
    db.create_all()
  server.run(debug=debug, host=host, port=port)