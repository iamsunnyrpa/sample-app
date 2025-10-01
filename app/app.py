from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route('/')
def hello():
    # Get a custom name from environment variable, default to 'world'
    name = os.environ.get("NAME", "world")
    # Get the hostname (container ID)
    hostname = socket.gethostname()
    
    html = f"<h3>Hello {name}!</h3>" \
           f"<b>Hostname:</b> {hostname}<br/>" \
           f"<b>Version:</b> 1.0.0"
    return html

if __name__ == "__main__":
    # Listen on all public IPs on port 5000
    app.run(host='0.0.0.0', port=5000)
