import src.module.image.service as ImageService;

from flask import request;
from src.module.server.initial import server;

@server.route('/upload-image', methods=['POST'])
def upload_image():
  return ImageService.upload_image(request)