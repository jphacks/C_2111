from wtfml.predictor.pred_onnx_model import OnnxPredictor

model_path = "./model/2021-10-24_distil/1/epoch=9-valid_loss=0.6320-valid_acc=1.0000_quant.onnx"
predictor = OnnxPredictor(model_path=model_path, device="cpu")

print(predictor.predict("今日も死にたい！")[0][0])