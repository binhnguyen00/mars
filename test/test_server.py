import unittest
import threading
import http.client
from src.module.server.server import run

class TestServer(unittest.TestCase):
  
  @classmethod
  def setUpClass(cls):
    # Start the server in a separate thread
    cls.server_thread = threading.Thread(target=run)
    cls.server_thread.setDaemon(True)
    cls.server_thread.start()

  def test_welcome_page(self):
    """Test the /welcome route.\n"""
    connection = http.client.HTTPConnection('localhost', 8000)
    connection.request('GET', '/welcome')
    response = connection.getresponse()
    
    self.assertEqual(response.status, 200)
    self.assertIn(b'<html>', response.read())  # Assuming your index.html starts with <html>

  def test_root_redirect(self):
    """Test that accessing root redirects to /welcome.\n"""
    connection = http.client.HTTPConnection('localhost', 8000)
    connection.request('GET', '/')
    response = connection.getresponse()
    
    self.assertEqual(response.status, 200)
    self.assertIn(b'<html>', response.read())  # Assuming your index.html starts with <html>

  def test_404(self):
    """Test that a non-existent path returns 404.\n"""
    connection = http.client.HTTPConnection('localhost', 8000)
    connection.request('GET', '/non-existent')
    response = connection.getresponse()
    
    self.assertEqual(response.status, 404)
    self.assertIn(b'404 Not Found', response.read())


if __name__ == '__main__':
  unittest.main()