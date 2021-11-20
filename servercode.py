#SERVER
import socket

host = 'localhost'
port = 5050

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))

s.listen(1)

c, addr = s.accept()

msg = c.recv(1024)

while msg:
	print("Received: " + msg.decode())
	msg = c.recv(1024)

c.close()