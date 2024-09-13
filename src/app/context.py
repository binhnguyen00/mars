import os

# Get the 'src' directory
SRC_DIR         = os.path.join(os.path.dirname(os.path.dirname(__file__)))

IMG_UPLOAD_DIR  = os.path.join(SRC_DIR, 'app/storage/image/uploads')
IMG_RESULT_DIR  = os.path.join(SRC_DIR, 'app/storage/image/results')

ARCHIVE_UPLOAD_DIR  = os.path.join(SRC_DIR, 'app/storage/archive/uploads')
ARCHIVE_RESULT_DIR  = os.path.join(SRC_DIR, 'app/storage/archive/results')

APP_CONFIG_DIR  = os.path.join(SRC_DIR, 'app/config/application.yaml')