import os
import socket
from flask import Flask, send_file

app = Flask(__name__)

# This tells Python to look for the HTML file in the CURRENT folder
HTML_FILE = 'anish_90day_bootcamp.html'

@app.route('/')
def home():
    if os.path.exists(HTML_FILE):
        return send_file(HTML_FILE)
    else:
        return f"<h1>Error: Could not find {HTML_FILE}</h1><p>Make sure the HTML file is in the same folder as this script.</p>"

if __name__ == '__main__':
    # Find your local IP address automatically
    hostname = socket.gethostname()
    try:
        ip_address = socket.gethostbyname(hostname)
    except:
        ip_address = "127.0.0.1"

    print(f"\n{'='*50}")
    print(f"✅ SERVER IS RUNNING!")
    print(f"{'='*50}")
    print(f"💻 On this Computer:  http://127.0.0.1:5000")
    print(f"📱 On Mobile (Same WiFi): http://{ip_address}:5000")
    print(f"{'='*50}\n")
    print("Press CTRL+C to stop the server.")
    
    # host='0.0.0.0' allows other devices on the network to connect
    app.run(host='0.0.0.0', port=5000, debug=True)