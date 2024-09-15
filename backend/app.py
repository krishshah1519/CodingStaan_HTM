from flask import Flask, request, jsonify
import requests
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app)  # Enable CORS to allow requests from your frontend

# Load the pre-trained ML model
model = joblib.load('model/model.pkl')  # Update the path to your model if necessary

# Google Gemini API key
gemini_api_key = 'AIzaSyBP3D3lL0pHtkCsttLeGMq1NMtp1RwcisA'  # Replace with your actual Gemini API key

@app.route('/api/personalized-questions', methods=['POST'])
def get_personalized_questions():
    data = request.json
    responses = data['responses']

    # Call Google Gemini API to get personalized questions
    api_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent"
    headers = {
        "Authorization": f"Bearer {gemini_api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "user_input": responses,  # Customize this according to the API spec if needed
        # Add any other required fields based on Gemini's API specification
    }

    try:
        # Send the POST request to Gemini API
        response = requests.post(api_url, json=payload, headers=headers)
        response.raise_for_status()  # Check for HTTP errors

        # Parse the response from Gemini API
        gemini_data = response.json()
        questions = gemini_data.get('questions', [])  # Extract the questions from the API response

        return jsonify({'questions': questions})

    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'API Request Error: {str(e)}'}), 500

@app.route('/api/quiz-results', methods=['POST'])
def get_quiz_results():
    data = request.json
    responses = data['responses']

    # Convert responses to numeric values for ML model
    numeric_responses = convert_to_numeric(responses)

    # Predict using the pre-trained ML model
    prediction = model.predict([numeric_responses])
    return jsonify({'results': prediction.tolist()})

def convert_to_numeric(responses):
    # Implement your conversion logic here
    return [float(response) for response in responses]  # Example conversion

if __name__ == '__main__':
    app.run(debug=True)
