import src.module.image.service as ImageService;

from flask import request;
from src.module.server.initial import server;

@server.route('/upload-image', methods=['POST'])
def upload_image():
  return ImageService.upload_image(request)

@server.route('/get-image/<image_name>', methods=['GET'])
def get_image(image_name):
  return ImageService.get_image(image_name)