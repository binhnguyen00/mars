import os;

from src.app.context import (SRC_DIR, IMG_RESULT_DIR, IMG_UPLOAD_DIR, ARCHIVE_RESULT_DIR, ARCHIVE_UPLOAD_DIR);

def create_storage_folder():
  os.makedirs(f"{SRC_DIR}/app/storage", exist_ok=True)

  os.makedirs(IMG_RESULT_DIR, exist_ok=True)
  os.makedirs(IMG_UPLOAD_DIR, exist_ok=True)

  os.makedirs(ARCHIVE_RESULT_DIR, exist_ok=True)
  os.makedirs(ARCHIVE_UPLOAD_DIR, exist_ok=True)