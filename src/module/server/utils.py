from http.server import HTTPServer;
from .server import Server;

def run(server_class=HTTPServer, handler_class=Server, port=8000) -> HTTPServer:
  server_address = ('', port)
  httpd = server_class(server_address, handler_class)
  print(f'Starting httpd server on port {port}...')
  httpd.serve_forever()
  return httpd