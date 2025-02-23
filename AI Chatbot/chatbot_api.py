from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load model
chatbot_model = joblib.load("T:\\TARUN LEARNING\\VITAGUARD AI APP\\AI Chatbot\\models\\chatbot.pkl")
vectorizer = joblib.load("T:\\TARUN LEARNING\\VITAGUARD AI APP\\AI Chatbot\\models\\chatbot_vectorizer.pkl")

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    query_vector = vectorizer.transform([data["query"]])
    response = chatbot_model.predict(query_vector)[0]
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
