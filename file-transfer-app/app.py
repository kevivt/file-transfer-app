from flask import Flask, request, render_template
import socket

app = Flask(__name__)

SERVER_IP = '192.168.181.168'  # Friend's PC IP
SERVER_PORT = 5001

@app.route('/')
def upload_form():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file:
        filename = file.filename
        file_data = file.read()

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((SERVER_IP, SERVER_PORT))
            s.sendall(filename.encode())
            s.sendall(file_data)

        return 'File uploaded successfully!'
    return 'No file uploaded.'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
