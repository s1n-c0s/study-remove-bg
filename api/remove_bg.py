from rembg import remove
from PIL import Image
import io
import base64
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/remove_bg', methods=['POST'])
def remove_bg():
    if 'image' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['image']
    input_image = Image.open(file)
    output_image = remove(input_image)

    # Convert to BytesIO
    img_io = io.BytesIO()
    output_image.save(img_io, format="PNG")
    img_io.seek(0)

    # Convert to base64
    img_base64 = base64.b64encode(img_io.read()).decode('utf-8')

    # Return as JSON
    return jsonify({'image': img_base64})

if __name__ == '__main__':
    app.run(debug=True)