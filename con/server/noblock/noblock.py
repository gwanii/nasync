# coding: utf-8

import fcntl
import os
import socket


response = 'HTTP/1.1 OK\r\nConnection: Close\r\nContent-Length: 1\r\n\r\nA'
server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('0.0.0.0', 8080))
server.listen(32)

import ipdb; ipdb.set_trace()  # XXX BREAKPOINT

flags = fcntl.fcntl(server.fileno(), fcntl.F_GETFL)
fcntl.fcntl(server.fileno(), fcntl.F_SETFL, flags | os.O_NONBLOCK)

clients = set([])


while True:
    try:
        client, clientaddr = server.accept()
        clients.add(client)
    except Exception as e:
        pass

    for client in clients.copy():
        try:
            request = client.recv(4096)
            client.send(response)
            clients.remove(client)
            client.close()
        except Exception as e:
            pass
