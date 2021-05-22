def gen_function(n):
    print('start')
    while n:
        print(f'yield: {n}')
        yield n
        n -= 1


a = gen_function(4)
print(a)
next(a)
next(a)
next(a)
next(a)


for i in gen_function(4):
    print(i)

c = [i for i in gen_function(9)]
print(c)

d = max(gen_function(8))
print(d)

x = [1, 2, 3, 4, 5,6]

listcomp = [i ** 2 for i in x]
print(listcomp)

gen = (i ** 2 for i in x)
print(gen)
print(f'ジェネレーター式{list(gen)}')


def change(list_):
    for lists in list_:
        for letter in lists:
            yield letter


list_ = 'Python', 'practice'
e = change(list_)
print(list(e))


def change_from(list_):
    for lists in list_:
        yield from (letter for letter in lists)


f = change_from(list_)
print(list(f))


def gen(n):
    while n:
        yield n
        n -= 1


x = [1, 2, 3, 4, 5, 6]
g = [i for i in zip(x, gen(max(x)))]
print(g)

odd = filter(lambda v: v % 2 == 1, gen(max(x)))
odd_ = [i for i in odd]
print(odd_)

h = gen(-1)
print(list(h))


def up(list):
    return list.upper()


a = up(list_)
print(a)
