import socket
def recvack(sock):
    sock.settimeout(1)
    try:
        ack,addr=sock.recvfrom(1024)
        return ack.decode()
    except socket.timeout:
        return None 

r=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
r.connect(('localhost',7000))
a=0
messages=['Hello','World','$']
for msg in messages:
    r.send((msg+str(a)).encode())
    print('Message Sent')
    ack=recvack(r)
    while not ack:
        print('No Acknowledgement. Retransmitting')
        r.send((msg+str(a)).encode())
        ack=recvack(r)
    if (a+1)%2==int(ack):
        print('Received Acknowledgement: ',ack)
        a=(a+1)%2
    else:
        print('Delayed Acknowledgement ')
r.close()