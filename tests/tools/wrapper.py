# tests/tools/wrapper.py

from functools import wraps

def it(description):
    def wrapper(func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            return func(*args, **kwargs)
        wrapped.__doc__ = description
        return wrapped
    return wrapper

def TestName(description):
    def wrapper(cls):
        cls.__doc__ = description
        return cls
    return wrapper
