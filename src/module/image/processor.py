import os
import imageio

from PIL import Image
from src.app.context import (IMG_RESULT_DIR, IMG_UPLOAD_DIR)

def sort(image_format: str) -> str:
  image_format = image_format.strip().lower()
  switcher = {
    "jpg": "process_image_jpg",
  }
  return switcher.get(image_format, "default")

def process_image(image_path: str, image_format: str):
  sorted = sort(image_format)
  result: None | str
  if sorted == "default":
    result = _process_image_default(image_path, image_format)
  elif sorted == "process_image_jpg":
    result = _process_image_jpg(image_path)

  return result


def _process_image_default(image_path: str, image_format: str):
  image_name, image_ext = os.path.splitext(os.path.basename(image_path)) # ('image', '.jpg')
  image_format = image_format.strip().lower()
  destination = os.path.join(IMG_RESULT_DIR, f"{image_name}.{image_format}")

  try:
    source = Image.open(image_path)
    if source.mode == 'RGBA': # If the image has an alpha channel (RGBA), convert it to RGB
      source = source.convert('RGB')
    source.save(destination, format=image_format.upper())
    print(f"Image saved successfully to {destination}")
    return destination
  except RuntimeError as e:
    print(f"An error occurred: {e}")
    return None

def _process_image_jpg(image_path: str):
  image_name, image_ext = os.path.splitext(os.path.basename(image_path)) # ('image', '.jpg')
  destination = os.path.join(IMG_RESULT_DIR, f"{image_name}.jpg")

  try:
    image = imageio.imread(image_path)
    imageio.imwrite(uri=destination, im=image)
    print(f"Image saved successfully to {destination}")
    return destination
  except RuntimeError as e:
    print(f"An error occurred: {e}")
    return None

def create_result_folder():
  os.makedirs(IMG_RESULT_DIR, exist_ok=True)

def create_storing_folder():
  os.makedirs(IMG_UPLOAD_DIR, exist_ok=True)