# coding: utf-8

import socket


response = 'HTTP/1.1 OK\r\nConnection: Close\r\nContent-Length: 1\r\n\r\nA'

server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('0.0.0.0', 8080))
server.listen(32)

while True:
    client, clientaddr = server.accept()
    request = client.recv(4096)
    client.send(response)
    client.close()
