def check_logged_in(func: object):
    def wrapper(*args, **kwargs):
        if "logged_in" in session:
            return func(*args, **kwargs)
        return "You are NOT logged in"
    return wrapper
