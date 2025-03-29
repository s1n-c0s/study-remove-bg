from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/remove_bg', methods=['POST'])
def remove_bg():
    try:
        # Set the content type explicitly
        response = jsonify({'error': 'Testing response format'})
        response.headers.set('Content-Type', 'application/json')
        return response
        
        # The actual code would be here once you confirm the response formatting works
        
    except Exception as e:
        # Ensure errors are also returned as JSON
        error_response = jsonify({'error': str(e)})
        error_response.headers.set('Content-Type', 'application/json')
        return error_response, 500

if __name__ == '__main__':
    app.run(debug=True)