import socket

s = socket.socket()
host = socket.gethostname()
port = 12345

s.connect()
print s.recv(1024)
s.close()
