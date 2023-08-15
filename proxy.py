import socket

def handle_request(client_socket, server_socket):
    # Get the request from the client
    request = client_socket.recv(1024)

    # Send the request to the server
    server_socket.send(request)

    # Get the response from the server
    response = server_socket.recv(1024)

    # Send the response to the client
    client_socket.send(response)

if __name__ == "__main__":
    # Create a socket for the client
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the local address and port
    client_socket.bind(("127.0.0.1", 8080))

    # Listen for connections from clients
    client_socket.listen(5)

    # Accept connections from clients
    while True:
        (client_socket, address) = client_socket.accept()

        # Get the server address and port from the request
        server_address = request.split(b" ")[1]
        server_port = request.split(b":")[1]

        # Create a socket for the server
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to the server
        server_socket.connect((server_address, server_port))

        # Handle the request
        handle_request(client_socket, server_socket)

        # Close the sockets
        client_socket.close()
        server_socket.close()
