from flask import Blueprint, request, jsonify
from career_prediction_model import predict_career

quiz_bp = Blueprint('quiz', __name__)

@quiz_bp.route('/predict', methods=['POST'])
def predict():
    data = request.json
    career_suggestions = predict_career(data)
    return jsonify({'careers': career_suggestions})
