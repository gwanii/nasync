from concurrent.futures import ThreadPoolExecutor
from requests_futures.sessions import FuturesSession
import time


urls = [
    'http://www.douban.com',
    'http://www.zhihu.com',
    'http://www.ustack.com',
    'http://www.dapenti.com',
]

time1 = time.time()
session = FuturesSession(executor=ThreadPoolExecutor(max_workers=10))
res = (session.get(u) for u in urls)
for r in res:
    print r.result().status_code
time2 = time.time()
print time2 - time1
