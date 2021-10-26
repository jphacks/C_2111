from flask import Flask, request, jsonify
import sys 
import json
sys.path.append("./")
from app.pytorch_utils import OnnxPredictor
from goo_lab.goo_apis import Goo

def load_model(model_path:str = "./onnx_model/epoch=9-valid_loss=0.6320-valid_acc=1.0000_quant.onnx"):
    predictor = OnnxPredictor(model_path=model_path, device="cpu")
    return predictor
model = load_model()
res = model.predict("今日も自殺")[0][0]

print(list(res))
data=json.dumps({"result":[float(i) for i in list(res)]}).encode()
print(data)

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    model = load_model()
    res = model.predict("今日も自殺")[0][0]
    res = json.dumps({"result":[float(i) for i in list(res)]}).encode()
    return res

@app.route('/goo', methods = ["POST"])
def textpair(text1:str, text2:str):
    textpair = Goo.textpair(text1, text2)
    return textpair
