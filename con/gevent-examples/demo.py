# coding: utf-8

import gevent


def foo():
    print 'Running in foo.'
    gevent.sleep(0)
    print 'Explicit context switch to foo again.'


def bar():
    print 'Explicit context switch to bar.'
    gevent.sleep(0)
    print 'Implicit context switch to bar'


gevent.joinall([
    gevent.spawn(foo),
    gevent.spawn(bar),
])
