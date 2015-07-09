__author__ = 'ed'
from functools import wraps

from .errors import forbidden
from flask.ext.login import current_user

def permission_required(f):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.is_anonymous():
                return forbidden('Insufficient permissions')
            return f(*args, **kwargs)
        return decorated_function
    return decorator
