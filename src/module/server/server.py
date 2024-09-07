import src.module.server.service as ServerService

from flask import (Flask, request)
from flask_cors import CORS

server = Flask(__name__)
CORS(server)

@server.route('/upload-image', methods=['POST'])
def upload_image():
  return ServerService.upload_image(request)

@server.route('/get-image/<image_name>', methods=['GET'])
def get_image(image_name):
  return ServerService.get_image(image_name)


def run(debug=True, host='0.0.0.0', port=5000):
  server.run(debug=debug, host=host, port=port)