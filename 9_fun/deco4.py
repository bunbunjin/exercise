from functools import wraps


def deco4(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        print('before exec')
        v = f(*args, **kwargs)
        print('after exec')
        return v
    return wrapper


@deco4
def func():
    """funcです"""
    print('exec')


func()
print(func.__name__, func.__doc__)
