import socket
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def decrypt(cp_text, key):
    iv = cp_text[:AES.block_size]
    cp = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cp.decrypt(cp_text[AES.block_size:]), AES.block_size)

# Configuration
HOST = 'localhost'
PORT = 8000

# Start listening for connections
receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
receiver_socket.bind((HOST, PORT))
receiver_socket.listen(1)

def generate_key():
    try:
        with open('key.txt', 'w') as f:
            f.write(os.urandom(16).hex())
    except:
        print("Error reading file 1")

def get_key():
    try:
        with open('key.txt', 'r') as f:
            v = f.read()
            #print(v)

            key = bytes.fromhex(v)
            return key
    except:
        print("Error reading file 2")

while True:
    generate_key()
    # Accept incoming connection
    sender_socket, sender_address = receiver_socket.accept()

    # Receive the encrypted data
    received_data = sender_socket.recv(1024)
    #print(received_data)
    #received_data=received_data.decode()
    received_data=decrypt(received_data,get_key())
    # Print the decrypted data
    #print("Received data:", received_data)
    decrypted_plaintext = received_data.decode()
    print("Received decrypted data:", decrypted_plaintext)

    # Close the connection
    sender_socket.close()
