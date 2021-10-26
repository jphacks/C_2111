from flask import Flask, request, jsonify
from pytorch_utils import load_model

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():


    return jsonify({"result":1})

