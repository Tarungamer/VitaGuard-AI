import json
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC

# Load dataset
with open("T:\\TARUN LEARNING\\VITAGUARD AI APP\\AI Chatbot\\medical_chatbot_data.json", "r") as file:
    data = json.load(file)

questions = [item["question"] for item in data]
answers = [item["answer"] for item in data]

# Train Model
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(questions)
model = SVC(kernel="linear")
model.fit(X, answers)

# Save Model
joblib.dump(model, "T:\\TARUN LEARNING\\VITAGUARD AI APP\\AI Chatbot\\models\\chatbot.pkl")
joblib.dump(vectorizer, "T:\\TARUN LEARNING\\VITAGUARD AI APP\\AI Chatbot\\models\\chatbot_vectorizer.pkl")
