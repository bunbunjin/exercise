from concurrent.futures import (ThreadPoolExecutor, as_completed)
from hashlib import md5
from pathlib import Path
from urllib import request
import time

urls = ['https://twitter.com',
        'https://www.facebook.com',
        'https://www.youtube.com',
        'https://qiita.com/']


def download(url):
    req = request.Request(url)
    name = md5(url.encode('utf-8')).hexdigest()
    file_path = './' + name
    with request.urlopen(req) as res:
        Path(file_path).write_bytes(res.read())
        return url, file_path


def elapased_time(f):
    def wrapper(*args, **kwargs):
        st = time.time()
        v = f(*args, **kwargs)
        print(f'{f.__name__}: {time.time() - st}')
        return v
    return wrapper


@elapased_time
def get_sequetial():
    for url in urls:
        print(download(url))


@elapased_time
def get_multi_thread():
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(download, url) for url in urls]
        for future in as_completed(futures):
            print(future.result())


get_sequetial()
get_multi_thread()
