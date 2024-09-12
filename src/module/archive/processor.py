import os;

from src.app.context import (ARCHIVE_RESULT_DIR, ARCHIVE_UPLOAD_DIR)

def create_result_folder():
  os.makedirs(ARCHIVE_RESULT_DIR, exist_ok=True)

def create_storing_folder():
  os.makedirs(ARCHIVE_UPLOAD_DIR, exist_ok=True)