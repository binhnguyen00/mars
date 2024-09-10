import yaml

from flask import Flask;
from flask_cors import CORS;

with open('src/app/config/application.yaml', 'r') as file:
  config = yaml.safe_load(file)

username = config['flask']['sqlalchemy']['username']
password = config['flask']['sqlalchemy']['password']
host = config['flask']['sqlalchemy']['host']
port = config['flask']['sqlalchemy']['port']
dbname = config['flask']['sqlalchemy']['dbname']
database_uri = f"postgresql://{username}:{password}@{host}:{port}/{dbname}"

server = Flask(__name__)
server.config["SQLALCHEMY_DATABASE_URI"] = database_uri
CORS(server)