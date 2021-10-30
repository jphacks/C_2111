import sys
sys.path.append("./")
from goo_lab.goo_apis import Goo
from bert.pytorch_utils import OnnxPredictor


def load_model(model_path:str = "./onnx_model/epoch=9-valid_loss=0.6226-valid_acc=0.8033.onnx"):
    predictor = OnnxPredictor(model_path=model_path, device="cpu")
    return predictor
model=load_model()
print(model.predict("田中さんに無視された。"))