# coding: utf-8

import Queue
import socket
import threading


response = 'HTTP/1.1 OK\r\nConnection: Close\r\nContent-Length: 1\r\n\r\nA'
server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('0.0.0.0', 8080))
server.listen(32)


def handler(queue):
    while True:
        client = queue.get()
        request = client.recv(4096)
        client.send(response)
        client.close()
    thread.exit()


queue = Queue.Queue()
threads = []


for i in range(0, 4):
    thread = threading.Thread(target=handler, args=(queue, ))
    thread.daemon = True
    thread.start()
    threads.append(thread)


while True:
    client, clientaddr = server.accept()
    queue.put(client)
