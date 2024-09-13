import os;
import imageio;
import uuid;
import src.module.database.connection as DatabaseConnect;

from PIL import Image as PILImage;
from src.app.context import (IMG_RESULT_DIR, IMG_UPLOAD_DIR);
from src.module.image.entity import Image;

def create_result_folder():
  os.makedirs(IMG_RESULT_DIR, exist_ok=True)

def create_storing_folder():
  os.makedirs(IMG_UPLOAD_DIR, exist_ok=True)

def save_uploaded_image(image_file): 
  try:
    image_name, image_ext = image_file.filename.rsplit('.', 1) # ('img_name_from_client', 'jpg')
    image_unique_name = uuid.uuid4().hex
    image_path = os.path.join(IMG_UPLOAD_DIR, f"{image_unique_name}.{image_ext}")

    # Save on disk
    image_file.save(image_path)

    # Save on database
    image = Image(name=image_unique_name)
    DatabaseConnect.insert(image)

    return image_unique_name, image_ext

  except RuntimeError as e:
    print(f"An error occurred: {e}")
    return None

def switch_method(image_format: str) -> str:
  image_format = image_format.strip().lower()
  scenario = {
    "jpg": "process_image_jpg",
  }
  return scenario.get(image_format, "process_image_default")

def process_image(image_unique_name: str, origin_format: str, target_format: str):
  scenario = switch_method(target_format)
  if (scenario == "process_image_default"): 
    result = _process_image_default(image_unique_name, origin_format, target_format)
  elif (scenario == "process_image_jpg"): 
    result = _process_image_jpg(image_unique_name, origin_format)
  else: 
    result = None
  return result

def _process_image_default(image_unique_name: str, origin_format: str, target_format: str):
  origin_format = origin_format.strip().lower()
  target_format = target_format.strip().lower()
  origin      = os.path.join(IMG_UPLOAD_DIR, f"{image_unique_name}.{origin_format}")
  destination = os.path.join(IMG_RESULT_DIR, f"{image_unique_name}.{target_format}")

  try:
    image = PILImage.open(origin)
    # If the image has an alpha channel (RGBA), convert it to RGB
    if image.mode == 'RGBA': 
      image = image.convert('RGB')
    # Save on disk
    image.save(destination, format=target_format.upper())
    # Save on database
    image = Image.get_by_name(image_unique_name)
    if image:
      image.result_format = target_format # type: ignore
      image.upload_format = origin_format # type: ignore
      DatabaseConnect.commit()

    return destination

  except RuntimeError as e:
    print(f"An error occurred: {e}")
    return None

def _process_image_jpg(image_unique_name: str, origin_format: str):
  origin_format = origin_format.strip().lower()
  target_format = "jpg"
  origin      = os.path.join(IMG_UPLOAD_DIR, f"{image_unique_name}.{origin_format}")
  destination = os.path.join(IMG_RESULT_DIR, f"{image_unique_name}.{target_format}")

  try:
    image = imageio.imread(origin)
    # Save on disk
    imageio.imwrite(uri=destination, im=image) 
    # Save on database
    image = Image.get_by_name(image_unique_name)
    if image:
      image.result_format = target_format # type: ignore
      image.upload_format = origin_format # type: ignore
      DatabaseConnect.commit()

    return destination

  except RuntimeError as e:
    print(f"An error occurred: {e}")
    return None