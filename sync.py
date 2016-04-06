import requests
import time


urls = [
    'http://www.douban.com',
    'http://www.zhihu.com',
    'http://www.ustack.com',
    'http://www.dapenti.com',
]

time1 = time.time()
for u in urls:
    print requests.get(u).status_code
time2 = time.time()
print time2 - time1
