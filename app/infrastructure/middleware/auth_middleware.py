# import jwt
from functools import wraps


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        return f(*args, **kwargs)

    return wrap
