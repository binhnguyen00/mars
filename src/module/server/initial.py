import yaml

from flask import Flask;
from flask_cors import CORS;
from src.app.context import APP_CONFIG_DIR

with open(APP_CONFIG_DIR, 'r') as file:
  config = yaml.safe_load(file)

sqlalchemy    = config['flask']['sqlalchemy']
username      = sqlalchemy['username']
password      = sqlalchemy['password']
host          = sqlalchemy['host']
port          = sqlalchemy['port']
dbname        = sqlalchemy['dbname']
database_uri  = f"postgresql://{username}:{password}@{host}:{port}/{dbname}"

server = Flask(__name__)
server.config["SQLALCHEMY_DATABASE_URI"] = database_uri
CORS(server)