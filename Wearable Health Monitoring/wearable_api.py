from flask import Flask, request, jsonify
import numpy as np
import joblib
import tensorflow as tf

app = Flask(__name__)

# Load Model
anomaly_model = tf.keras.models.load_model("models/anomaly_detector.h5")

@app.route('/wearable-monitor', methods=['POST'])
def monitor():
    data = np.array(request.json["vitals"]).reshape(1, -1)
    anomaly_score = anomaly_model.predict(data)
    status = "Alert: Possible health issue detected!" if anomaly_score > 0.5 else "Normal"
    return jsonify({"status": status})

if __name__ == '__main__':
    app.run(debug=True, port=5002)
