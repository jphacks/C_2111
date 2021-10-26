from bert.wtfml.predictor.pred_onnx_model import OnnxPredictor

def load_model():
    model_path = "../onnx_model/epoch=9-valid_loss=0.6320-valid_acc=1.0000_quant.onnx"
    predictor = OnnxPredictor(model_path=model_path, device="cpu")

    return predictor