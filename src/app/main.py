from src.module.server.service import run_server;
from src.app.service import create_storage_folder;

if __name__ == '__main__':
  create_storage_folder()
  run_server(debug=True, host='localhost', port=5000)