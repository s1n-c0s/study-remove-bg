import requests
import json
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Replace with your actual API key
REMOVE_BG_API_KEY = 'YOUR_API_KEY'

@app.route('/remove_bg', methods=['POST'])
def remove_bg():
    try:
        if 'image' not in request.files:
            return jsonify({'error': 'No file part'}), 400

        file = request.files['image']
        
        # Send to remove.bg API
        response = requests.post(
            'https://api.remove.bg/v1.0/removebg',
            files={'image_file': file},
            data={'size': 'auto'},
            headers={'X-Api-Key': REMOVE_BG_API_KEY},
        )
        
        if response.status_code == 200:
            # Return the base64 encoded image directly
            img_base64 = response.json().get('data', {}).get('b64_image')
            return jsonify({'image': img_base64})
        else:
            return jsonify({'error': f'API Error: {response.text}'}), response.status_code

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)