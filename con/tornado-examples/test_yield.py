# coding: utf-8


class ReturnEx(Exception):

    def __init__(self, value=None):
        super(ReturnEx, self).__init__()
        self.value = value
        self.args = (value, )


def test_yield():
    print 's:before 1'
    yield 1
    print 's:1'
    yield 2
    print 's:2'
    yield 3
    print 's:3'
    aaa = (yield 4)
    print aaa
    print 's:4'
    yield 5
    raise ReturnEx(1)


if __name__ == '__main__':
    c = test_yield()
    print c.next()
    print c.next()
    print c.next()
    print c.send('continue')  # if not, will not print 's:3'
    c.send('continue')
    try:
        a = c.send('')
    except ReturnEx as e:
        print e.value
