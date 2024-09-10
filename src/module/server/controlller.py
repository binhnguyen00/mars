import src.module.server.service as ServerService;

from flask import request;
from src.module.server.initial import server;

@server.route('/upload-image', methods=['POST'])
def upload_image():
  return ServerService.upload_image(request)

@server.route('/get-image/<image_name>', methods=['GET'])
def get_image(image_name):
  return ServerService.get_image(image_name)