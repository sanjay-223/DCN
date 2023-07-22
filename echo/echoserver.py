import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('localhost',7000))
print('socket created')

while True:
    msg,addr=s.recvfrom(1024)
    s.connect(addr)
    print('Received Message: ', msg.decode())
    s.send(msg)
    print('message sent')