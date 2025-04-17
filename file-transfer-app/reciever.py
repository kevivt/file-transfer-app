# server.py
import socket
import os

HOST = '192.XXX.XXX.XXX'  # Server's IP address (his)
PORT = 5001

save_dir = 'received_files'
os.makedirs(save_dir, exist_ok=True)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    print(f"[+] Waiting for connection on {HOST}:{PORT}...")
    conn, addr = s.accept()
    print(f"[+] Connected by {addr}")

    with conn:
        filename = conn.recv(1024).decode()
        print(f"[+] Receiving file: {filename}")
        filepath = os.path.join(save_dir, filename)

        with open(filepath, 'wb') as f:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                f.write(data)

        print("[+] File received and saved.")
