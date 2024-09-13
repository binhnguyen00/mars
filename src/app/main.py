from src.module.server.service import run_server;
from src.app.service import create_storage_folder;

def main():
  create_storage_folder()
  run_server(debug=True, host='localhost', port=5000)

if __name__ == '__main__':
  main()