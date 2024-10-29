import socket
from des_module import decrypt

def server_program():
    # Set up the server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1", 65432))
    server_socket.listen(1)

    print("Waiting for connection...")
    conn, addr = server_socket.accept()
    print(f"Connected by: {addr}")

    # Receive encrypted message
    encrypted_message = conn.recv(1024)
    print(f"Encrypted message received: {encrypted_message}")

    # Decrypt the message
    decrypted_message = decrypt(encrypted_message)
    print(f"Decrypted message: {decrypted_message}")

    conn.close()

if __name__ == "__main__":
    server_program()
