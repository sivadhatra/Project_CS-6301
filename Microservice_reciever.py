import socket

# Configuration
HOST = 'localhost'
PORT = 8000

# Start listening for connections
receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
receiver_socket.bind((HOST, PORT))
receiver_socket.listen(1)

while True:
    # Accept incoming connection
    sender_socket, sender_address = receiver_socket.accept()

    # Receive the encrypted data
    received_data = sender_socket.recv(1024)
    received_data=received_data.decode()
    # Print the decrypted data
    print("Received data:", received_data)

    # Close the connection
    sender_socket.close()
