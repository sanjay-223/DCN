import socket

def get_webpage(url):
    protocol_end = url.find("://")
    if protocol_end == -1:
        print("Invalid URL format. Please include the protocol (e.g., 'http://').")
        return

    url = url[protocol_end + 3:]
    host_end = url.find("/")
    if host_end == -1:
        host = url
        path = "/"
    else:
        host = url[:host_end]
        path = url[host_end:]

    server_port = 80
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, server_port))
    except socket.error as e:
        print(f"Error connecting to {host}: {e}")
        return

    # Prepare the HTTP request
    request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\n\r\n"

    try:
        # Send the request to the server
        client_socket.sendall(request.encode())

        # Receive and print the response
        response = b""
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            response += data

        # Close the socket
        client_socket.close()

        # Extract and print the webpage content
        response = response.decode(errors='ignore')  # Decode the response bytes to a string
        content_start = response.find("\r\n\r\n") + 4
        webpage_content = response[content_start:]
        print(webpage_content)

    except socket.error as e:
        print(f"Error while receiving data: {e}")

if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/Reims_Cathedral"
    get_webpage(url)
