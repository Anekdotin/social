__author__ = 'ed'
from app import app
DEBUG = True
PORT = 8080
HOST = '0.0.0.0'


if __name__ == '__main__':
    app.run(debug=DEBUG)
