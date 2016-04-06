from twisted.internet.task import react
import treq


def print_response(x):
    print(x.code)

def main(reactor, *args):
    d = treq.get('http://www.douban.com')
    d.addCallback(print_response)
    return d

react(main, [])
