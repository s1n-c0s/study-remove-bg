from flask import Flask, request, send_file, jsonify
import cv2
import numpy as np
from rembg import remove
from PIL import Image
import io

app = Flask(__name__)

@app.route('/api/remove_bg', methods=['POST'])
def remove_bg():
    if 'image' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    image = request.files['image'].read()
    img = Image.open(io.BytesIO(image))
    
    # Remove background
    output = remove(img)
    
    # Save to BytesIO
    img_io = io.BytesIO()
    output.save(img_io, format='PNG')
    img_io.seek(0)
    
    return send_file(img_io, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
