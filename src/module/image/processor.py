import os
import cv2

from src.app.context import RESULT_FOLDER

def process_image(image_path: str, image_format: str) -> str:
  image_name, image_ext = os.path.splitext(os.path.basename(image_path)) # ('image', '.jpg')
  image_format = image_format.strip().lower()

  destination = os.path.join(RESULT_FOLDER, f"{image_name}.{image_format}")
  source = cv2.imread(image_path)
  if source is not None:
    success = cv2.imwrite(destination, source)
    if success:
      print(f"Image saved successfully to {destination}")
    else:
      print("Failed to save the image")
  else:
    print("Failed to load the image")

  return destination