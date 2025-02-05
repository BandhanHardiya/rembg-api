# test_app.py
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    port = os.environ.get("PORT", 8000)
    return f"Test server running on port {port}!"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))
    print(f"Starting server on port {port}")  # Debug log
    app.run(host='0.0.0.0', port=port, debug=True)
