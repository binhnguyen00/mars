import os;
import imageio;
import uuid;
import src.module.database.connection as DatabaseConnect;

from PIL import Image as PILImage;
from src.app.context import (IMG_RESULT_DIR, IMG_UPLOAD_DIR);
from src.module.image.table.image import Image;

def create_result_folder():
  os.makedirs(IMG_RESULT_DIR, exist_ok=True)

def create_storing_folder():
  os.makedirs(IMG_UPLOAD_DIR, exist_ok=True)

def save_image(image_file): 
  try:
    image_name, image_ext = image_file.filename.rsplit('.', 1) # ('image', 'jpg')
    image_unique_name = uuid.uuid4().hex
    image_path = os.path.join(IMG_UPLOAD_DIR, f"{image_unique_name}.{image_ext}")

    # Save on disk
    image_file.save(image_path)

    # Save on database
    image = Image(name=image_unique_name, path=image_path)
    DatabaseConnect.insert(image)

    return image_path

  except RuntimeError as e:
    print(f"An error occurred: {e}")
    return None

def switch_method(image_format: str) -> str:
  image_format = image_format.strip().lower()
  scenario = {
    "jpg": "process_image_jpg",
  }
  return scenario.get(image_format, "process_image_default")

def process_image(image_path: str, image_format: str):
  scenario = switch_method(image_format)
  if (scenario == "process_image_default"): 
    result = _process_image_default(image_path, image_format)
  elif (scenario == "process_image_jpg"): 
    result = _process_image_jpg(image_path)
  return result

def _process_image_default(image_path: str, image_format: str):
  destination = _find_destination(image_path, image_format)

  try:
    source = PILImage.open(image_path)
    if source.mode == 'RGBA': # If the image has an alpha channel (RGBA), convert it to RGB
      source = source.convert('RGB')
    source.save(destination, format=image_format.upper())
    print(f"Image saved successfully to {destination}")
    return destination
  except RuntimeError as e:
    print(f"An error occurred: {e}")
    return None

def _process_image_jpg(image_path: str):
  destination = _find_destination(image_path, "jpg")

  try:
    image = imageio.imread(image_path)
    imageio.imwrite(uri=destination, im=image)
    print(f"Image saved successfully to {destination}")
    return destination
  except RuntimeError as e:
    print(f"An error occurred: {e}")
    return None

def _find_destination(image_path: str, image_format: str):
  image_name, image_ext = os.path.basename(image_path).rsplit('.', 1) # ('image', 'jpg')
  image_format = image_format.strip().lower()
  destination = os.path.join(IMG_RESULT_DIR, f"{image_name}.{image_format}")
  return destination