from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Change this route to match what's expected
@app.route('/', methods=['POST'])  # Note: Use root path for Vercel serverless functions
def remove_bg():
    try:
        if 'image' not in request.files:
            return jsonify({'error': 'No file part'}), 400

        # Just for testing - return success without processing
        return jsonify({'success': True, 'message': 'API endpoint is working'})
        
        # Actual implementation would go here
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# This is required for Vercel serverless functions
app = app.wsgi_app