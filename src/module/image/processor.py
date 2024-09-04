import shutil
from src.app.context import (RESULT_FOLDER)

def process_image(image_path: str, image_name: str):
  source = image_path + '/' + image_name
  result = RESULT_FOLDER + '/' + image_name
  shutil.copy(source, result)