from concurrent.futures import (ThreadPoolExecutor, wait)
import threading


class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count = self.count + 1


class ThreadSafeCounter:
    lock = threading.Lock()

    def __init__(self):
        self.count = 0

    def increment(self):
        with self.lock:
            self.count = self.count + 1


def count_up(counter):
    for _ in range(1000000):
        counter.increment()


counter = Counter()
threads = 2
with ThreadPoolExecutor() as e:
    futures = [e.submit(count_up, counter) for _ in range(threads)]
    done, not_done = wait(futures)

print(f'{counter.count=:,}')

counter_ = ThreadSafeCounter()
threads_ = 4
with ThreadPoolExecutor() as e:
    futures = [e.submit(count_up, counter_) for _ in range(threads_)]
    done, not_done = wait(futures)

print(f'{counter_.count=:}')
