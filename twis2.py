#!/usr/bin/python2.7

from twisted.internet import reactor
from twisted.internet.defer import Deferred, DeferredList, DeferredLock
from twisted.internet.defer import inlineCallbacks
from twisted.web.client import Agent, HTTPConnectionPool
from twisted.web.http_headers import Headers
from pprint import pprint
from collections import defaultdict
from urlparse import urlparse
from random import randrange
import fileinput

pool = HTTPConnectionPool(reactor)
pool.maxPersistentPerHost = 16
agent = Agent(reactor, pool)
locks = defaultdict(DeferredLock)
codes = {}

def getLock(url, simultaneous = 1):
    return locks[urlparse(url).netloc, randrange(simultaneous)]

@inlineCallbacks
def getMapping(url):
    # Limit ourselves to 4 simultaneous connections per host
    # Tweak this number, but it should be no larger than pool.maxPersistentPerHost
    lock = getLock(url,4)
    yield lock.acquire()
    try:
        resp = yield agent.request('HEAD', url)
        codes[url] = resp.code
    except Exception as e:
        codes[url] = str(e)
    finally:
        lock.release()


dl = DeferredList(getMapping(url.strip()) for url in fileinput.input())
dl.addCallback(lambda _: reactor.stop())

reactor.run()
pprint(codes)
