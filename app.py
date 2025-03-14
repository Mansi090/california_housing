import pickle
from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the model
model = pickle.load(open('regmodel.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')  # Ensure home.html is inside 'templates/' folder

@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.json['data']
    print("Received Data:", data)
    
    try:
        data_array = np.array(list(data.values())).reshape(1, -1)
        output = model.predict(data_array)
        print("Predicted Output:", output[0])
        return jsonify({"prediction": output[0]})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
