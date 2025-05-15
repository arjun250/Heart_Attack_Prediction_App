# Heart Attack Risk Prediction

A web-based machine learning app that predicts the likelihood of a heart attack using logistic regression.

## Features
- Logistic Regression (NumPy)
- Gradient Descent
- Flask API
- HTML + JS Frontend

## How to Run
1. Train the model in Jupyter and save weights: `np.save("model.npy", theta_opt)`
2. Run Flask backend:
   ```bash
   python app.py
