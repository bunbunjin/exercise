class Iterable:
    def __init__(self, num):
        self.num = num

    def __iter__(self):
        return iter(range(self.num))


a = [val for val in Iterable(3)]
print(a)

