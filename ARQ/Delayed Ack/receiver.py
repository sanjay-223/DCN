import socket
import time

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('localhost',7000))
print('socket created')
ack=0
i=1
fno=''
while True:
    msg,addr=s.recvfrom(1024)
    msg=msg.decode()
    msg,fno=msg[:-1],msg[-1]
    print('Received Message: ', msg)
    s.connect(addr)
    ack=(ack+1)%2
    i+=1
    if i==2:
        time.sleep(1.1)

    if ack==(fno):
        s.send(str(ack).encode())
    else:
        print('duplicate frame')

        s.send(str(ack).encode())
    print('Acknowledgement Sent')
    if msg=='$':
        print('Transmission End')
        break