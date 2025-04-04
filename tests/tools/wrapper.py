def it(description):
    def wrapper(func):
        func.__doc__ = description
        return func
    return wrapper

def TestName(description):
    def wrapper(func):
        func.__doc__ = description
        return func
    return wrapper