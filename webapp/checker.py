from flask import session
from functools import wraps

"""decorator function to check if we are logged in"""

def check_logged_in(func: object):
    @wraps(func)
    def wrapper(*args, **kwargs):

        if "logged_in" in session:
            return func(*args, **kwargs)
        return "You are not logged in"

    return wrapper
