# Echo client program
import time
import socket

HOST = '127.0.0.1'
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, 60003))
s.connect((HOST, PORT))
s.sendall('Hello, world.')
data = s.recv(1024)
print 'Received', repr(data)
time.sleep(2.0)
s.close()
