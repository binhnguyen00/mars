import os

ROOT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__))) # Get the 'src' directory
UPLOAD_DIR = os.path.join(ROOT_DIR, 'module/image/resources/uploads')
RESULT_DIR = os.path.join(ROOT_DIR, 'module/image/resources/results')
APP_CONFIG_DIR = os.path.join(ROOT_DIR, 'app/config/application.yaml')