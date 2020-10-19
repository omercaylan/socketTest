

#!/usr/bin/env python3

import socket
test = '192.168.0.102'
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 7        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((test, PORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024)

print('Received', repr(data))