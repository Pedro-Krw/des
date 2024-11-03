from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import socket
import threading

# untuk DEAS
KEY = b'secret_k'

# ////
def encrypt_message(message):
    cipher = DES.new(KEY, DES.MODE_ECB)
    # Pesan 
    encrypted_message = cipher.encrypt(pad(message.encode(), 8))
    return encrypted_message  # Mengembalikan pesan terenkripsi

# Fungsi dekripsi pesan  DES
def decrypt_message(encrypted_message):
    cipher = DES.new(KEY, DES.MODE_ECB)
    # Unpad pesan setelah didekripsi
    decrypted_message = unpad(cipher.decrypt(encrypted_message), 8)
    return decrypted_message.decode()  # Mengembalikan pesan asli

# bagian ini jalankan server
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345)) 
    server_socket.listen(1)
    print("Server berjalan dan menunggu koneksi...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Terhubung dengan {addr}")

        
        encrypted_message = client_socket.recv(1024)
        
        # pesan ditampilkan
        decrypted_message = decrypt_message(encrypted_message)
        print("Pesan diterima:", decrypted_message)

        client_socket.close()

# Fungsi untuk menjalankan client
def start_client():
    # Input pesan dari pengguna
    message = input("Masukkan pesan untuk dienkripsi: ")

    # Enkripsi pesan
    encrypted_message = encrypt_message(message)


    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))
    client_socket.sendall(encrypted_message)

    client_socket.close()
    print("Pesan terenkripsi telah dikirim.")


def main():
    role = input("Masukkan 's' untuk menjalankan sebagai server, atau 'c' untuk client: ").strip().lower()
    if role == 's':
        start_server()
    elif role == 'c':
        start_client()
    else:
        print("Input tidak valid. Silakan masukkan 's' atau 'c'.")


if __name__ == "__main__":
    main()
