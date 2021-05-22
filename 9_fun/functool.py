from functools import lru_cache
from time import sleep

@lru_cache(maxsize=32)
def heavy_funcion(n):
    sleep(3)
    return n + 1

a = heavy_funcion(2)
print(a)
aa = a
print(aa)


