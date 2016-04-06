# -*- coding: utf-8 -*-
# from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
import time
import urllib2

urls = [
    'http://www.douban.com',
    'http://www.douban.com',
    'http://www.douban.com',
    'http://www.douban.com',
    'http://www.douban.com',
    'http://www.douban.com',
    'http://www.douban.com',
    'http://www.douban.com',
    'http://www.douban.com',
    'http://www.douban.com',
    'http://www.douban.com',
    'http://www.douban.com',
    'http://www.douban.com',
    'http://www.douban.com',
    'http://www.douban.com',
    'http://www.douban.com',
    'http://www.douban.com',
    'http://www.douban.com',
    'http://www.douban.com',
    'http://www.douban.com',
    'http://www.douban.com',
    'http://www.douban.com',
    'http://www.douban.com',
    'http://www.douban.com',
    'http://www.douban.com',
    'http://www.douban.com',
    'http://www.douban.com',
    'http://www.douban.com',
    'http://www.douban.com',
]

start = time.time()
results = map(urllib2.urlopen, urls)
print 'Normal:', time.time() - start

start2 = time.time()
pool = ThreadPool(processes=4)
results2 = pool.map(urllib2.urlopen, urls)
pool.close()
pool.join()
print 'Thread Pool:', time.time() - start2

start3 = time.time()
pool = ThreadPool(processes=8)
results3 = pool.map(urllib2.urlopen, urls)
pool.close()
pool.join()
print 'Thread Pool:', time.time() - start3

start4 = time.time()
pool = ThreadPool(processes=12)
results4 = pool.map(urllib2.urlopen, urls)
pool.close()
pool.join()
print 'Thread Pool:', time.time() - start4
