from flask import Flask, request, jsonify, render_template
import os
import socket

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Socket settings
SERVER_IP = "192.168.7.168"
SERVER_PORT = 5001
SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    uploaded_file = request.files.get("file")
    if uploaded_file:
        path = os.path.join(UPLOAD_FOLDER, uploaded_file.filename)
        uploaded_file.save(path)

        try:
            filesize = os.path.getsize(path)
            filename = os.path.basename(path)

            s = socket.socket()
            s.connect((SERVER_IP, SERVER_PORT))
            s.send(f"{filename}{SEPARATOR}{filesize}\n".encode())  # send header

            with open(path, "rb") as f:
                while True:
                    bytes_read = f.read(BUFFER_SIZE)
                    if not bytes_read:
                        break
                    s.sendall(bytes_read)

            s.close()
            return jsonify({"message": "File uploaded and sent!"})
        except Exception as e:
            print(f"[!] Socket error: {e}")
            return jsonify({"message": f"Upload saved but sending failed: {e}"}), 500

    return jsonify({"message": "No file received"}), 400

if __name__ == "__main__":
    app.run(debug=True)
