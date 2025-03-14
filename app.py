import pickle
from flask import Flask, request, jsonify, render_template
import numpy as np

app = Flask(__name__)

# Load the model
model = pickle.load(open('regmodel.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')  # Ensure home.html is inside 'templates/' folder

@app.route('/predict_api', methods=['POST'])
def predict_api():
    try:
        data = request.json.get("data", {})  # Get JSON safely
        print("Received Data:", data)

        # Convert input to numpy array
        data_array = np.array(list(data.values())).reshape(1, -1)

        # Directly predict without scaling
        output = model.predict(data_array)
        print("Predicted Output:", output[0])

        return jsonify({"prediction": float(output[0])})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Convert form input to float list
        data = [float(x) for x in request.form.values()]
        data_array = np.array(data).reshape(1, -1)

        # Directly predict without scaling
        output = model.predict(data_array)[0]
        return render_template('home.html', prediction_text=f'Predicted House Price: $ {output:.2f}')
    except Exception as e:
        return render_template('home.html', prediction_text=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
