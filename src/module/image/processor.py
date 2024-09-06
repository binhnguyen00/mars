import os
from PIL import Image

from src.app.context import RESULT_FOLDER

def process_image(image_path: str, image_format: str) -> str:
  print(image_format)
  image_name, image_ext = os.path.splitext(os.path.basename(image_path)) # ('image', '.jpg')
  image_format = image_format.strip().lower()
  destination = os.path.join(RESULT_FOLDER, f"{image_name}.{image_format}")

  try:
    source = Image.open(image_path)
    if source.mode == 'RGBA': # If the image has an alpha channel (RGBA), convert it to RGB
      source = source.convert('RGB')
    source.save(destination, format=image_format.upper())
    print(f"Image saved successfully to {destination}")
  except Exception as e:
    print(f"Failed to process the image: {e}")

  return destination