# coding: utf-8

import socket
import sys
import multiprocessing


response = 'HTTP/1.1 OK\r\nConnection: Close\r\nContent-Length: 1\r\n\r\nA'
server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('0.0.0.0', 8080))
server.listen(32)


def handler():
    while True:
        client, addr = server.accept()
        request = client.recv(4096)
        client.send(response)
        client.close()
    sys.exit()


processes = []
for i in range(0, 4):
    process = multiprocessing.Process(target=handler, args=())
    process.start()
    processes.append(process)

for process in processes:
    process.join()
