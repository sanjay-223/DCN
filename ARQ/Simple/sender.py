import socket

r=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
r.connect(('localhost',7000))
data = ['Hello','World','$']
for d in data:
    r.send(d.encode())
    print('Message send')
    msg1,addr=r.recvfrom(1024)
    print('Acknowledgement : ',msg1.decode())