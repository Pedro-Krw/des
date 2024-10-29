from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

# Hardcoded DES key (8 bytes)
KEY = b'8bytekey'

def encrypt(message):
    cipher = DES.new(KEY, DES.MODE_ECB)
    padded_message = pad(message.encode(), DES.block_size)
    encrypted_message = cipher.encrypt(padded_message)
    return encrypted_message

def decrypt(encrypted_message):
    cipher = DES.new(KEY, DES.MODE_ECB)
    decrypted_message = unpad(cipher.decrypt(encrypted_message), DES.block_size)
    return decrypted_message.decode()

# sender

import socket
from des_module import encrypt

def client_program():
    # Set up the client
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 65432))

    # Get input from user
    message = input("Enter a message to encrypt and send: ")

    # Encrypt the message
    encrypted_message = encrypt(message)
    print(f"Encrypted message to send: {encrypted_message}")

    # Send encrypted message
    client_socket.sendall(encrypted_message)

    client_socket.close()

if __name__ == "__main__":
    client_program()
