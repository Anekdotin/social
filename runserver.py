__author__ = 'ed'
import os

DEBUG = True
PORT = 8080
HOST = '0.0.0.0'
from app import create_app

app = create_app(os.getenv('FLASK_CONFIG') or 'default')


if __name__ == '__main__':
    app.run(debug=DEBUG)
