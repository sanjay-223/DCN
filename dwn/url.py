import socket
import ssl
from urllib.parse import urlparse

def download_webpage(url):
    parsed_url = urlparse(url)
    hostname = parsed_url.hostname
    path = parsed_url.path or "/"

    context = ssl.create_default_context()

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ssl_sock = context.wrap_socket(sock, server_hostname=hostname)
    ssl_sock.connect((hostname, 443))

    request = f"GET {path} HTTP/1.1\r\nHost: {hostname}\r\n\r\n"
    ssl_sock.send(request.encode())

    response = b""
    while True:
        data = ssl_sock.recv(4096)
        if not data:
            break
        response += data
    
    response = response.decode("utf-8", errors="ignore")
    headers, _, content = response.partition("\r\n\r\n")
    return content


url = input("Enter URL (preferably simple): ")
webpage_content = download_webpage(url)
print("\n\n\nWeb Page Coding :",webpage_content)