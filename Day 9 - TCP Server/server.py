import sys
import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(("127.0.0.1", 9999))
s.listen(1)

print("Server listening.....")

conn, addr = s.accept()
print(f"Connection from {addr}")

data = conn.recv(1024)
print(f"The data recieved {data}")

conn.send(b"Hello Client")

conn.close()
s.close()
