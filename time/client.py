import socket

r=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
r.connect(('localhost',7000))
while True:
    msg1=input("Enter message : ")
    r.send(msg1.encode())
    msg1,addr=r.recvfrom(1024)
    print('listening')
    print('current date and time is : ',msg1.decode())
r.close()