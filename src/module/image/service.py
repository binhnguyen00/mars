import os;
import src.module.image.processor as ImgProcessor;

from flask import (Request, jsonify, send_file);
from src.app.context import (IMG_UPLOAD_DIR, IMG_RESULT_DIR);

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
    file_path = os.path.join(IMG_UPLOAD_DIR, file.filename)
    file.save(file_path)
    result_image = ImgProcessor.process_image(file_path, format)
    if result_image is not None:
      response = send_file(result_image, as_attachment=True)
      return response
    else:
      return jsonify({
        'error': 'Failed to process image'
      }), 500


def get_image(image_name):
  directory = os.path.join(IMG_RESULT_DIR, image_name)
  print(directory)
  return send_file(directory, as_attachment=True)