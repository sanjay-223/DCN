import socket

def download_webpage(url):
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Set a timeout of 5 seconds (adjust as needed)
    client_socket.settimeout(5)

    try:
        # Connect to the web server on port 80
        client_socket.connect((url, 80))

        # Send an HTTP GET request
        request = f"GET / HTTP/1.1\r\nHost: {url}\r\n\r\n"
        client_socket.send(request.encode())

        # Receive the response from the server
        response = b""
        while True:
            data = client_socket.recv(4096)
            if not data:
                break
            response += data
            #print(data.decode())


    except socket.timeout:
        pass
    
    finally:
        # Close the socket
        client_socket.close()

    # Extract the HTML content from the response
    html = response.decode()

    return html

# Example usage
url = "www.example.com"
html = download_webpage(url)
print(html)
