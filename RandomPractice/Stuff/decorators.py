class decorator_class(object):

    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print("call method calling {} before".format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)

def decorator_function(original_function):
    def wrapper(*args, **kwargs):
        print("THis is extra functionality!!")
        return original_function(*args, **kwargs)
    return wrapper()

@decorator_class
def defy():
    print("Hello from defy")


