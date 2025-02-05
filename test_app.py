# test_app.py
from flask import Flask, request, send_file
from rembg import remove
from io import BytesIO
import os

app = Flask(__name__)

@app.route('/')
def home():
    port = os.environ.get("PORT", 8000)
    return f"Background Removal API is running on port {port}!"

@app.route('/remove-bg', methods=['POST'])
def remove_bg():
    if 'image' not in request.files:
        return {"error": "No image uploaded"}, 400
    
    try:
        image_file = request.files['image']
        input_image = image_file.read()
        output_image = remove(input_image)
        output_io = BytesIO(output_image)
        output_io.seek(0)
        return send_file(output_io, mimetype='image/png')
    except Exception as e:
        print(f"Error processing image: {str(e)}")  # Debug log
        return {"error": "Failed to process image"}, 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))
    print(f"Starting server on port {port}")  # Debug log
    app.run(host='0.0.0.0', port=port, debug=True)
