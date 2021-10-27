from django.shortcuts import render
from pytorch_utils import OnnxPredictor

def index(request):
    return render(request, 'index.html')

def load_model(model_path:str = "./onnx_model/epoch=9-valid_loss=0.6320-valid_acc=1.0000_quant.onnx"):
    predictor = OnnxPredictor(model_path=model_path, device="cpu")
    return predictor

print(load_model().predict("日本"))