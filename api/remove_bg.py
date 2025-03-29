from rembg import remove
from PIL import Image
import io
import base64
import traceback
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/remove_bg', methods=['POST'])
def remove_bg():
    try:
        if 'image' not in request.files:
            return jsonify({'error': 'No file part'}), 400

        file = request.files['image']
        
        # Ensure the file is not empty
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400

        # Open the image
        input_image = Image.open(file.stream)
        
        # Remove background
        output_image = remove(input_image)

        # Convert to BytesIO
        img_io = io.BytesIO()
        output_image.save(img_io, format="PNG")
        img_io.seek(0)

        # Convert to base64
        img_base64 = base64.b64encode(img_io.read()).decode('utf-8')

        # Return as JSON
        return jsonify({'image': img_base64})

    except Exception as e:
        # Log the full error for debugging
        print(f"Error processing image: {str(e)}")
        print(traceback.format_exc())
        
        # Return a generic error response
        return jsonify({
            'error': 'Failed to process image',
            'details': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True)