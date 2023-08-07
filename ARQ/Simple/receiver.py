import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('localhost',7000))
print('socket created')
ack=0
while True:
    msg,addr=s.recvfrom(1024)
    print('Received Message: ', msg.decode())
    s.connect(addr)
    ack=(ack+1)%2
    s.send(str(ack).encode())
    print('Acknowledgement Sent')
    if msg.decode()=='$':
        print('Transmission End')
        break