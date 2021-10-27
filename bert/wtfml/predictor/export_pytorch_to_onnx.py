#%%
from typing import Optional
import os 
working_direction = os.getcwd()
import sys
sys.path.append(working_direction)
import torch
from transformers import DistilBertTokenizer
from wtfml.engine.nlp.model import  DistilBERTBaseClassifier
from wtfml.engine.pl_engine.DistilBERT_classification import DistilBERTClassificationPlEngine


pl_model_path = "model/2021-10-27_distil/epoch=9-valid_loss=0.6226-valid_acc=0.8033.ckpt" #TODO:pathの変更
onnx_save_path = None
is_bert_model: bool = False
is_optimeze: bool = False and is_bert_model  # if you use BERT model you can set True
is_quantize: bool = True

onnx_save_path = onnx_save_path or ".".join(pl_model_path.split(".")[:-1]) + ".onnx"

classification_model = DistilBERTBaseClassifier(num_classes=2)
tokenizer = DistilBertTokenizer.from_pretrained(
    "cl-tohoku/bert-base-japanese-whole-word-masking"
)
pl_engine = DistilBERTClassificationPlEngine(model=classification_model)
pl_engine.load_from_checkpoint(pl_model_path, model=classification_model)
pl_engine.eval()
onnx_save_path = onnx_save_path or ".".join(pl_model_path.split(".")[:-1]) + ".onnx"

symbolic_names = {0: "batch_size", 1: "max_seq_len"}
inputs = tokenizer.encode_plus(
    "ONNXのエクスポートのためのSample Inputの作成をここでしています",
    None,
    add_special_tokens=True,
    truncation=True,
)

ids = torch.tensor(inputs["input_ids"], dtype=torch.long).unsqueeze(0)
mask = torch.tensor(inputs["attention_mask"], dtype=torch.long).unsqueeze(0)

torch.onnx.export(
    pl_engine,
    (ids, mask, ),
    onnx_save_path,
    input_names=["ids", "mask",],
    export_params=True,
    output_names=["output"],
    opset_version=12,
    dynamic_axes={
        "ids": symbolic_names,  # variable length axes
        "mask": symbolic_names,
        "output": {0: "batch_size"},
    },
)
#%%
if is_optimeze:
    from onnxruntime.transformers import optimizer

    optimized_model_path = (
        ".".join(onnx_save_path.split(".")[:-1])
        + "_opt."
        + onnx_save_path.split(".")[-1]
    )
    optimized_model = optimizer.optimize_model(
        onnx_save_path, model_type="bert", num_heads=12, hidden_size=768
    )
    optimized_model.save_model_to_file(optimized_model_path)
#%%
if is_quantize:
    import onnx
    from onnxruntime.quantization import QuantType, quantize_dynamic

    model_fp32_path = optimized_model_path if is_optimeze else onnx_save_path
    model_quant_path = (
        ".".join(model_fp32_path.split(".")[:-1])
        + "_quant."
        + model_fp32_path.split(".")[-1]
    )
    if is_bert_model:
        quantize_dynamic(model_fp32_path, model_quant_path, weight_type=QuantType.QInt8)
    else:
        quantize_dynamic(model_fp32_path, model_quant_path)
