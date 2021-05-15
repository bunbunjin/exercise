class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Pont({self.x}, {self.y})'

    def __str__(self):
        return f'({self.x}, {self.y})'


s = 'string'
p = Point(1, 2)
print(p)
print(p)
