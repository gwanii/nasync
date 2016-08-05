import gevent
from gevent.queue import Queue

count_quque = Queue()
students_total = 0

def blackboard():
    while not count_queue.empty():
        n = count_queue.get()
        students_total += n
        print('Erasing... Now total number of students is: %s' % students_total)
        gevent.sleep(0)

def teacher1(n):
    for i in xrange(1,n):
        count_queue.put_nowait(1)
        print('Teacher 1: so far I have counted %s students, where is the next one?’)

def teacher2(n):
    for i in xrange(1,n):
        count_queue.put_nowait(1)
        print('Teacher 2: so far I have counted %s students, where is the next one?’)

gevent.spawn(teacher1, 25).join()
gevent.spawn(teacher2, 25).join()

gevent.joinall([
    gevent.spawn(blackboard),
])
