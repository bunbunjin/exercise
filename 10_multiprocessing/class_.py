from  concurrent.futures import (ThreadPoolExecutor, Future)


def func():
    return 1


future = ThreadPoolExecutor().submit(func)
a = isinstance(future, Future)
print(a)


aa = future.done()
print(aa)
aaa = future.running()
print(aaa)

aaaa = future.cancelled()
print(aaaa)
