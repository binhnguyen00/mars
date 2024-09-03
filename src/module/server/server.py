import os;
from http.server import (BaseHTTPRequestHandler, HTTPServer);

class Server(BaseHTTPRequestHandler):

  def do_GET(self) -> None:
    if self.path == '/':
      self.path = '/welcome'
    try:
      if self.path == '/welcome':
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))  # Get the 'src' directory
        file_path = os.path.join(base_dir, 'ui', 'public', 'index.html')
        with open(file_path, 'r') as file:
          page = file.read()
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes(page, 'utf-8'))

      else:
        self.send_response(404)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'404 Not Found')

    except Exception as ex:
      self.send_error(500, f"Internal Server Error: {str(ex)}")


def run(server_class=HTTPServer, handler_class=Server, port=8000):
  server_address = ('', port)
  httpd = server_class(server_address, handler_class)
  print(f'Starting httpd server on port {port}...')
  httpd.serve_forever()