class A:
    def __len__(self):
        return 6


class B:
    def __len__(self):
        return -1


a = A()
print(len(a))

b = B()
print(len(b))
