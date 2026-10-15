
from flask import Flask, request, jsonify
import joblib
import numpy as np
from datetime import datetime
import os

app = Flask(__name__)

model = joblib.load("iris_model.pkl")
LOG_FILE = "/var/log/ml_api.log"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    if not data or 'features' not in data:
        return jsonify({"error": "Provide a features array"}), 400

    features = np.array(data['features'], dtype=float)

    if features.shape != (4,):
        return jsonify({
            "error": "Exactly four flower measurements are required"
        }), 400

    prediction = model.predict(features.reshape(1, -1))[0]

    log = {
        "timestamp": datetime.utcnow().isoformat(),
        "input": features.tolist(),
        "prediction": str(prediction)
    }

    with open(LOG_FILE, 'a') as f:
        f.write(str(log) + "\n")

    return jsonify({"prediction": str(prediction)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

