import pickle
from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = pd.DataFrame(data)
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    predictions = model.predict(features)
    return jsonify(predictions.tolist())

if __name__ == '__main__':
    app.run(debug=True)
