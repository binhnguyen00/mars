import src.module.image.processor as ImgProcessor;

from src.module.database.db import db;
from src.module.server.initial import server;

def run_server(debug=False, host='0.0.0.0', port=5000):
  ImgProcessor.create_result_folder()
  ImgProcessor.create_storing_folder()
  with server.app_context():
    db.create_all()
  server.run(debug=debug, host=host, port=port)