import socket 
import datetime

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('localhost',7000))
print('connection established')

msg1,addr=s.recvfrom(1024)

if(msg1.decode()=='date'):
    s.connect(addr)
    curr=datetime.datetime.now()
    msg=str(curr)
    s.send(msg.encode())
    print('message sent')
s.close()