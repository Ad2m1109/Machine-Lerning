from flask import Flask, request, jsonify
import joblib
import numpy as np

# Load the trained model
model = joblib.load("gradient_boosting_model.pkl")

# Create a Flask app
app = Flask(__name__)

# Define a route for the root URL
@app.route('/', methods=['GET'])
def home():
    return "Welcome to the California Housing Price Prediction API! Use the /predict endpoint to get predictions."

# Define a route for making predictions
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the input data from the request
        data = request.get_json()

        # Check if 'features' key exists in the input data
        if 'features' not in data:
            return jsonify({'error': 'Missing "features" key in input data'}), 400

        # Convert features to a numpy array
        features = np.array(data['features']).reshape(1, -1)

        # Check if the number of features matches the model's expectations
        if features.shape[1] != 8:
            return jsonify({'error': 'Invalid number of features. Expected 8.'}), 400

        # Make a prediction
        prediction = model.predict(features)

        # Return the prediction as a JSON response
        return jsonify({'prediction': prediction.tolist()})

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)