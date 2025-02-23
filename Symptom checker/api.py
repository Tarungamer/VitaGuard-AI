from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load trained model
model = joblib.load("T:\\TARUN LEARNING\\VITAGUARD AI APP\\Symptom checker\\models\\disease_predictor.pkl")
label_encoder = joblib.load("T:\\TARUN LEARNING\\VITAGUARD AI APP\\Symptom checker\\models\\label_encoder.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    symptoms = pd.DataFrame([data["symptoms"]])  # Convert input to DataFrame

    # Prediction
    probabilities = model.predict_proba(symptoms)[0]
    top_indices = probabilities.argsort()[-3:][::-1]
    top_diseases = label_encoder.inverse_transform(top_indices)

    return jsonify({
        "top_diseases": list(top_diseases),
        "confidence": list(probabilities[top_indices])
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
