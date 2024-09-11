import os

# Get the 'src' directory
SRC_DIR         = os.path.join(os.path.dirname(os.path.dirname(__file__)))

IMG_UPLOAD_DIR  = os.path.join(SRC_DIR, 'module/image/resources/uploads')
IMG_RESULT_DIR  = os.path.join(SRC_DIR, 'module/image/resources/results')
APP_CONFIG_DIR  = os.path.join(SRC_DIR, 'app/config/application.yaml')