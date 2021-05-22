def deco1(f):
    print('deco1 called')

    def wrapper():
        print('before exec')
        v = f()
        print('afttr exec')
        return v
    return wrapper


@deco1
def func():
    print('exec')
    return 1


print(func.__name__)
print(func())


def deco2(f):
    print('deco2 called')

    def wrapper(*args, **kwargs):
        print('before exec')
        v = f(*args, **kwargs)
        print('after exec')
        return v
    return wrapper


@deco2
def func(x, y):
    print('exec')
    return x, y


aa = func(2, 4)
print(aa)


def deco3(z):
    def _deco3(f):
        def wrapper(*args, **kwargs):
            print('before exec', z)
            v = f(*args, **kwargs)
            print('after exec', z)
            return v
        return wrapper
    return _deco3


@deco3(z=3)
def func(x, y):
    print('exec')
    return x, y


bb = func(1, 2)
print(bb)

@deco3(z=3)
@deco3(z=4)
def func(x, y):
    print("exec")
    return x, y


print(func(1, 2))
