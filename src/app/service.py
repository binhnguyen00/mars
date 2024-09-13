import os;

from src.app.context import SRC_DIR;
import src.module.image.processor as ImgProcessor;
import src.module.archive.processor as ArchiveProcessor;

def create_storage_folder():
  os.makedirs(f"{SRC_DIR}/app/storage", exist_ok=True)
  ImgProcessor.create_result_folder()
  ImgProcessor.create_storing_folder()
  ArchiveProcessor.create_result_folder()
  ArchiveProcessor.create_storing_folder()