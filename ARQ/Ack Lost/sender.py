import socket


def send(sock,msg):
    sock.send(msg.encode())
    
def recvack(sock):
    sock.settimeout(2)
    try:
        ack,addr=sock.recvfrom(1024)
        return ack.decode()
    except socket.timeout:
        return None 

r=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
r.connect(('localhost',7000))
#message='Once upon a time there lived a ghost. He was known to be a killer and feared the most'
#messages=message.split()
messages=['Hello','World','This','is','python','$']
for msg in messages:
    send(r,msg)
    print('Message Sent')
    ack=recvack(r)
    if isinstance(ack,str):
        print('Received Acknowledgement: ',ack)
    else:
        print('No Acknowledgement. Retransmitting')
        send(r,msg)      