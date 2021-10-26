from flask import Flask, request, jsonify
# from app.bert.wtfml.predictor.pred_onnx_model import OnnxPredictor

# def load_model(model_path:str = "./onnx_model/epoch=9-valid_loss=0.6320-valid_acc=1.0000_quant.onnx"):
#     predictor = OnnxPredictor(model_path=model_path, device="cpu")
#     return predictor

from app.goo_lab import goo_apis

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():

    return jsonify({"result":1})
