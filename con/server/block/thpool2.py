# coding: utf-8

import socket
import threading


response = 'HTTP/1.1 200 OK\r\nConnection: Close\r\nContent-Length: 1\r\n\r\nA'
server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('0.0.0.0', 8080))
server.listen(32)


def handler():
    while True:
        client, clientaddr = server.accept()
        client.recv(4096)
        client.send(response)
        client.close()
    thread.exit()


threads = []
for i in range(0, 4):
    thread = threading.Thread(target=handler, args=())
    thread.start()
    threads.append(thread)


for thread in threads:
    thread.join()
