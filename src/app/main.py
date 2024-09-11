from src.module.server.service import run_server as run

if __name__ == '__main__':
  run(debug=True, host='localhost', port=5000)