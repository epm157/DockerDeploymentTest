'''


import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle



app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    int_features = [x for x in request.form.values()]
    final_features = [np.array(int_features)]
    predection = model.predict(final_features)
    output = round(predection[0], 2)
    return render_template('index.html', prediction_text=f'Employee Salary should be $ {output}')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.get_json(force=True)
    features = data.values()
    features = list(features)
    features = [np.array(features)]
    prediction = model.predict(features)
    output = prediction[0]
    result = jsonify(output)
    return result


if __name__ == "__main__":
    app.rum(debug=True)
'''


