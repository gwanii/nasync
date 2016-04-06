import tornado.ioloop
from tornado.httpclient import AsyncHTTPClient


urls = [
    'http://www.douban.com',
    'http://www.zhihu.com',
    'http://www.ustack.com',
    'http://www.dapenti.com',
]

i = 0

def handle_request(response):
    global i
    print response.code
    if i == 3:
        tornado.ioloop.IOLoop.instance().stop()
    i += 1

httpclient = AsyncHTTPClient()
for u in urls:
    httpclient.fetch(u, handle_request)

tornado.ioloop.IOLoop.instance().start()
