from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import os

app = Flask(__name__)
CORS(app)

# ✅ Load model weights and normalization parameters
model_dir = r"C:\Users\ARJUN CHAURASIYA\OneDrive\Desktop\Heart Attack Prediction"
theta = np.load(os.path.join(model_dir, "model.npy"))
means = np.load(os.path.join(model_dir, "means.npy"))
stds = np.load(os.path.join(model_dir, "stds.npy"))

# ✅ Sigmoid function
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    age = float(data["age"])
    sysBP = float(data["sysBP"])
    prevalentHyp = float(data["prevalentHyp"])

    # ✅ Normalize using saved means and stds
    age_norm = (age - means[0]) / stds[0]
    sysBP_norm = (sysBP - means[1]) / stds[1]
    prevalentHyp_norm = (prevalentHyp - means[2]) / stds[2]

    # ✅ Create input vector with bias
    X = np.array([1, age_norm, sysBP_norm, prevalentHyp_norm])
    probability = sigmoid(np.dot(X, theta))
    prediction = int(probability >= 0.5)

    return jsonify({
        "prediction": prediction,
        "probability": round(float(probability), 4)
    })

if __name__ == "__main__":
    app.run(debug=True)
