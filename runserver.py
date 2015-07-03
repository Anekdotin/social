__author__ = 'ed'

DEBUG = True
PORT = 8080
HOST = '0.0.0.0'

from app import app

if __name__ == '__main__':
    app.run(debug=DEBUG)
