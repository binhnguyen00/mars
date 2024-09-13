from src.module.database.initial import db;
from src.module.server.initial import server;

def run_server(debug=False, host='0.0.0.0', port=5000):
  # Component Scan
  import src.module.archive.controller;
  import src.module.image.controlller;
  from src.module.image.entity import Image
  from src.module.archive.entity import Archive 

  with server.app_context():
    db.create_all()
    print("Tables created successfully")
    
  server.run(debug=debug, host=host, port=port)