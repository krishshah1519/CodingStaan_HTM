from flask import Blueprint, request, jsonify
from model import predict_career
import requests

quiz_bp = Blueprint('quiz', __name__)

# Route for predicting career based on responses
@quiz_bp.route('/predict', methods=['POST'])
def predict():
    try:
        # Ensure request data is in JSON format
        data = request.json
        if not data:
            return jsonify({'error': 'No input data provided'}), 400
        
        # Input validation: Ensure required fields are present
        if 'responses' not in data:
            return jsonify({'error': '"responses" field is required'}), 400

        responses = data['responses']

        # Make sure responses are a list
        if not isinstance(responses, list):
            return jsonify({'error': '"responses" must be a list'}), 400

        # Call the model prediction function
        career_suggestions = predict_career(responses)
        
        # Return the prediction as a JSON response
        return jsonify({'careers': career_suggestions}), 200
    
    except Exception as e:
        # Catch any exceptions and return an error message
        return jsonify({'error': str(e)}), 500

# Route for generating questions using Gemini API
@quiz_bp.route('/generate_questions', methods=['POST'])
def generate_questions():
    try:
        # Ensure request data is in JSON format
        data = request.json
        if not data:
            return jsonify({'error': 'No input data provided'}), 400

        # Input validation: Ensure required fields are present
        if 'input' not in data:
            return jsonify({'error': '"input" field is required'}), 400

        user_input = data['input']

        # Make request to the Gemini API for question generation
        api_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent"  # Update with actual Gemini API endpoint
        headers = {"Authorization": "AIzaSyBP3D3lL0pHtkCsttLeGMq1NMtp1RwcisA"}  # Replace with your Gemini API key

        payload = {
            "user_input": user_input,
            # Add any other required fields based on Gemini's API specification
        }

        # Send POST request to Gemini API
        response = requests.post(api_url, json=payload, headers=headers)
        response.raise_for_status()  # Raise exception for HTTP errors

        # Parse the response from Gemini API
        gemini_data = response.json()

        # Return the generated questions
        return jsonify(gemini_data), 200
    
    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'API Request Error: {str(e)}'}), 500
    
    except Exception as e:
        # Catch other exceptions and return an error message
        return jsonify({'error': str(e)}), 500
