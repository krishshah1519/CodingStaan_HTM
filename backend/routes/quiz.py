from flask import Blueprint, request, jsonify
from model import predict_career

quiz_bp = Blueprint('quiz', __name__)

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

        # Make sure responses are a dictionary
        if not isinstance(responses, dict):
            return jsonify({'error': '"responses" must be a dictionary'}), 400

        # Call the model prediction function
        career_suggestions = predict_career(responses)
        
        # Return the prediction as a JSON response
        return jsonify({'careers': career_suggestions}), 200
    
    except Exception as e:
        # Catch any exceptions and return an error message
        return jsonify({'error': str(e)}), 500
