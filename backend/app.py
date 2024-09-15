from flask import Flask, request, jsonify
import openai
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app)  # Enable CORS to allow requests from your frontend

# Load the pre-trained ML model
model = joblib.load('backend/model/model.pkl')  # Update the path to your model if necessary

# OpenAI API key
openai.api_key = 'YOUR_OPENAI_API_KEY'  # Replace with your actual OpenAI API key

@app.route('/api/personalized-questions', methods=['POST'])
def get_personalized_questions():
    data = request.json
    responses = data['responses']

    # Call OpenAI/Gemini API to get personalized questions
    response = openai.Completion.create(
        engine="text-davinci-003",  # Use the appropriate model engine
        prompt=f"Generate personalized questions based on the following responses: {responses}",
        max_tokens=150
    )
    questions = response.choices[0].text.strip().split('\n')
    return jsonify({'questions': questions})

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
     