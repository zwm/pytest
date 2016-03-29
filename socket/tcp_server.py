# Echo server program
import socket

HOST = '127.0.0.1'
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
j = 1
while 1:
    conn, addr = s.accept()
    print 'Connected by', addr
    i = 1
    while 1:
            print "---------------------------------------"
            print "Receive Time:", i
            print "---------------------------------------"
            data = conn.recv(1024)
            print "Receive Data:", data
            print ""
            if not data: break
            conn.sendall(data)
            i+=1
    j += 1
    if j == 5: break
conn.close()

