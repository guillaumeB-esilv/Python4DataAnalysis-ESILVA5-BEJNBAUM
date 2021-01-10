from flask import Flask
from flask import request, redirect, url_for, flash, jsonify
import numpy as np
import pickle as p
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, send_wildcard=True)

@app.route('/api/', methods=['POST'])
def makecalc():
    data = request.get_json()
    prediction = np.array2string(model.predict(data))

    return jsonify(prediction)
    
if __name__ == '__main__':
    modelfile = 'final_prediction.pickle'
    model = p.load(open(modelfile, 'rb'))
    app.run(debug=True)