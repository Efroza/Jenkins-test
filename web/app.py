# app.py
import signal
import sys
from flask import Flask

app = Flask(__name__)

# Define the shutdown function to stop the Flask app gracefully
def shutdown_server(signal, frame):
    print("Received stop signal. Shutting down the server...")
    sys.exit(0)

# Register the shutdown function to handle SIGINT signal (Ctrl+C)
signal.signal(signal.SIGINT, shutdown_server)

@app.route('/')
def hello():
    return "Hello, World!"

@app.route('/stop')
def stop_server():
    shutdown_server(None, None)
    return "Server stopped successfully!"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
