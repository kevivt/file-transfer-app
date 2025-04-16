# File Transfer App 📁

A simple web-based file transfer application using Flask (for frontend) and raw TCP sockets (for backend).

## Features
- Upload files via a clean HTML interface
- Files sent to another device on the same hotspot/network
- Progress bar, status message, and file validation

## Technologies
- Flask (Python)
- Raw socket programming
- HTML/CSS

## How to Run
1. Start the server on the receiving device:
    ```bash
    python receiver.py
    ```
2. Start the Flask app on the sender's device:
    ```bash
    python app.py
    ```
3. Access the interface at: `http://localhost:5000`
