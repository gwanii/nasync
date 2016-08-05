# coding: utf-8

import datetime
from functools import wraps
import time

import tornado
from tornado import gen, options, define


define("port", default=8000, help="run on the given port", type=int)


def sync_loop_call(delta=60 * 1000):
    """
    Wait for func down then process add_timeout
    """
    def wrap_loop(func):
        @wraps(func)
        @gen.coroutine
        def wrap_func(*args, **kwargs):
            options.logger.info("function %r start at %d" %
                                (func.__name__, int(time.time())))
            try:
                yield func(*args, **kwargs)
            except Exception, e:
                options.logger.error("function %r error: %s" %
                                     (func.__name__, e))
            options.logger.info("function %r end at %d" %
                                (func.__name__, int(time.time())))
            tornado.ioloop.IOLoop.instance().add_timeout(
                datetime.timedelta(milliseconds=delta),
                wrap_func)
        return wrap_func
    return wrap_loop


@sync_loop_call(delta=10 * 1000)
def worker():
    """
    Do something
    """
    pass


if __name__ == "__main__":
    worker()
    tornado.options.parse_command_line()
    app = tornado.web.Application()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)

    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
