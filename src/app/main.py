from src.module.server.service import run_server

if __name__ == '__main__':
  run_server(debug=True, host='localhost', port=5000)