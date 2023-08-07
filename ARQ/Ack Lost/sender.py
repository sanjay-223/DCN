import socket
def recvack(sock):
    sock.settimeout(2)
    try:
        ack,addr=sock.recvfrom(1024)
        return ack.decode()
    except socket.timeout:
        return None 

r=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
r.connect(('localhost',7000))

messages=['Hello','World','$']
for msg in messages:
    r.send(msg.encode())
    print('Message Sent')
    ack=recvack(r)
 
    while not ack:
        print('No Acknowledgement. Retransmitting')
        r.send(msg.encode())
        ack=recvack(r)
    print('Received Acknowledgement: ',ack)
r.close()