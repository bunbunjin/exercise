class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __setattr__(self, name, value):
        if name not in ('x', 'y'):
            raise AttributeError('Not allowed')
        super().__setattr__(name, value)


p = Point(1, 2)

p.x = 3


