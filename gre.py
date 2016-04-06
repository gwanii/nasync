import time
import grequests


urls = [
    'http://www.douban.com',
    'http://www.zhihu.com',
    'http://www.ustack.com',
    'http://www.dapenti.com',
]

time1 = time.time()
rs = (grequests.get(u) for u in urls)
for i in grequests.imap(rs):
    print i.status_code
time2 = time.time()
print time2 - time1
