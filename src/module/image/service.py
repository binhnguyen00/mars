import src.module.image.processor as ImgProcessor;

from flask import (Request, jsonify, send_file);

def upload_image(request: Request):
  if 'image' not in request.files:
    return jsonify({
      'error': 'No image part in the request'
    }), 400

  file          = request.files['image']
  target_format = request.form.get('format') or 'PNG'
  if file.filename == '' or not file.filename:
    return jsonify({
      'error': 'No selected file'
    }), 400
  else:
    image = ImgProcessor.save_uploaded_image(file)
    if image is not None:
      image_unique_name, origin_format = image
    if image_unique_name is not None:
      result_image = ImgProcessor.process_image(image_unique_name, origin_format, target_format)
    if result_image is not None:
      response = send_file(result_image, as_attachment=True)
      return response
    else:
      return jsonify({
        'error': 'Failed to process image'
      }), 500