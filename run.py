__author__ = 'ed'

DEBUG = True
PORT = 8080
HOST = '0.0.0.0'

from app import app
app.run(debug=DEBUG, host=HOST, port=PORT)
