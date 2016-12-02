#!/usr/bin/env python 

""" 
A simple echo server 
""" 

import socket 

host = '' 
port = 50000 
backlog = 5 
size = 1024 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind((host,port)) 
s.listen(backlog) 
while 1: 
    try:
        client, address = s.accept()
    except KeyboardInterrupt:
        print 'Keyboard interrupt detected, exiting...'
        exit(0)
        s.close() 
    print 'New connection received: ' + address
    data = client.recv(size) 
    if data: 
        client.send(data) 
    client.close()