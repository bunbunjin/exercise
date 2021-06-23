import asyncio
import random


async def coro():
    return 'bunbunjin'


a = asyncio.run(coro())
print(a)


async def call_web_api(url):
    print(f'send a request: {url}')
    await asyncio.sleep(random.random())
    print(f'got a response: {url}')
    return url


async def async_download(url):
    response = await call_web_api(url)
    return response


result = asyncio.run(
    async_download('https://twitter.com/home')
)


async def main():
    task = asyncio.gather(
        async_download('https://twitter.com/home'),
        async_download('https://www.youtube.com/'),
        async_download('https://abema.tv/video'),
    )
    return await task

results = asyncio.run(main())
print(results)


async def coro(n):
    await asyncio.sleep(n)
    return n


async def main():
    task = asyncio.create_task(coro(1))
    print(task)
    return await task

aa = asyncio.run(main())
print(aa)


async def main():
    task1 = asyncio.create_task(coro(1))
    task2 = asyncio.create_task(coro(2))
    task3 = asyncio.create_task(coro(3))
    print(await task1)
    print(await task2)
    print(await task3)

asyncio.run(main())


async def main():
    print(await coro(1))
    print(await coro(2))
    print(await coro(3))

asyncio.run(main())
