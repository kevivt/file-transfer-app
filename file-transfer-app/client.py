import socket
import os

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096
SERVER_IP = "192.168.181.168"  # Friend's IP (check it!)
SERVER_PORT = 5001

def send_file(filepath):
    try:
        filesize = os.path.getsize(filepath)
        filename = os.path.basename(filepath)

        s = socket.socket()
        s.connect((SERVER_IP, SERVER_PORT))
        s.send(f"{filename}{SEPARATOR}{filesize}".encode())

        with open(filepath, "rb") as f:
            while True:
                bytes_read = f.read(BUFFER_SIZE)
                if not bytes_read:
                    break
                s.sendall(bytes_read)

        s.close()
        print(f"[+] Sent {filename}")
        return True
    except Exception as e:
        print(f"[!] Error: {e}")
        return False
