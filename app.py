from flask import Flask, request, send_file, render_template
from rembg import remove
from PIL import Image
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/remove_bg', methods=['POST'])
def remove_bg():
    if 'image' not in request.files:
        return "No file uploaded", 400

    file = request.files['image']
    input_image = Image.open(file)
    output_image = remove(input_image)

    img_io = io.BytesIO()
    output_image.save(img_io, format="PNG")
    img_io.seek(0)

    return send_file(img_io, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
