import asyncio
import aiohttp

urls = [
    'http://www.douban.com',
    'http://www.zhihu.com',
    'http://www.ustack.com',
    'http://www.dapenti.com',
]

async def fetch_page(session, url):
    with aiohttp.Timeout(10):
        async with session.get(url) as response:
            return await response.read()

loop = asyncio.get_event_loop()
with aiohttp.ClientSession(loop=loop) as session:
    for u in urls:
        print(loop.run_until_complete(fetch_page(session, u)))
