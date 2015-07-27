__author__ = 'ed'
WTF_CSRF_ENABLED = False
SECRET_KEY = 'you-will-never-guess'
import os


basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')


# upload images

UPLOAD_FOLDER = '/home/ed/Development/Python/social/profilepics'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])




# email server
MAIL_SERVER = 'your.mailserver.com'
MAIL_PORT = 25
MAIL_USE_TLS = False
MAIL_USE_SSL = False
MAIL_USERNAME = 'you'
MAIL_PASSWORD = 'your-password'

# administrator list
ADMINS = ['eddwinn@example.com']

# pagination
POSTS_PER_PAGE = 3
MAX_SEARCH_RESULTS = 50

FLASKY_FOLLOWERS_PER_PAGE = 50
FLASKY_COMMENTS_PER_PAGE = 30

