from flask import Flask
import socket
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    hostname = socket.gethostname()
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"<h1>Hello from {hostname}!</h1><p>Server time: {current_time}</p><p>Nick's first app is running.</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
