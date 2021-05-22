from dataclasses import dataclass


with open('some.txt', 'w') as f:
    f.write('Bunbunjin')

print(f.closed)


class ContextManager:
    def __enter__(self):
        print("__enter__ was called")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__ was called')
        print(f'{exc_type=}')
        print(f'{exc_val=}')
        print(f'{exc_tb=}')


with ContextManager():
    print('inside the block')
    # 1/0 テキストの例外の出方のやつ


class AsTest:
    def __enter__(self):
        return 1

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


with AsTest() as x:
    print(x)

with AsTest():
    pass


class Point:
    def __init__(self, **kwargs):
        self.value = kwargs

    def __enter__(self):
        print('__enter__ was called')
        return self.value

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__ was called')
        print(self.value)


with Point(x=1, y=2) as p:
    print(p)
    p['z'] = 3


from contextlib import contextmanager


@contextmanager
def point(**kwargs):
    print('__enter__ was called')
    value = kwargs
    try:
        yield value
    except Exception as e:
        print(e, 'called')
        raise
    finally:
        print('__exit__ was called')
        print(value)


with point(x=2, y=5) as p:
    print(p)
    p['z'] = 5


