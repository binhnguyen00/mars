import os
import unittest
import requests

from image.service import run_server

class TestServer(unittest.TestCase):

  @classmethod
  def setUpClass(cls):
    run_server(debug=True, host='localhost', port=5001) # Start the server before tests run

  def test_server_is_running(self): 
    response = requests.get('http://localhost:5001/')
    self.assertEqual(response.status_code, 200)

  def test_upload_image(self):
    image_path = os.path.join(os.path.dirname(__file__), 'resources', 'doge.jpg')
    self.assertTrue(os.path.exists(image_path), "Test image does not exist")

    files = {'image': open(image_path, 'rb')}
    response = requests.post('http://localhost:5001/upload-image', files=files)
    files['image'].close()
    self.assertEqual(response.status_code, 200)
    self.assertIn('Image uploaded successfully', response.json()['message'])

    saved_file_path = response.json()['file_path']
    self.assertTrue(os.path.exists(saved_file_path), f"File was not saved: {saved_file_path}")

if __name__ == '__main__':
  unittest.main()