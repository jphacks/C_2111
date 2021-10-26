import numpy as np
import os
import onnxruntime
from transformers import DistilBertTokenizer
from wtfml.data_loaders.nlp.utils import clean_sentence
from wtfml.utils.utils import np_softmax


class OnnxPredictor:
    def __init__(
        self,
        model_path: str,
        device="cpu",
        tokenizer_name="cl-tohoku/bert-base-japanese-whole-word-masking",
        clearning_function=clean_sentence,
    ):

        self.tokenizer = DistilBertTokenizer.from_pretrained(tokenizer_name)
        self.clearning_function = clearning_function
        sess_options = onnxruntime.SessionOptions()
        sess_options.graph_optimization_level = (
            onnxruntime.GraphOptimizationLevel.ORT_ENABLE_ALL
        )
        if device == "cpu":
            providers = ["CPUExecutionProvider"]
        else:
            raise ValueError(
                "GPUのONNXランタイムはしないです。"
            )
        self.session = onnxruntime.InferenceSession(
            model_path, sess_options, providers=providers
        )
        self.device = device

    def predict(self, text: str):
        if self.clearning_function:
            text = self.clearning_function(text)

        inputs = self.tokenizer.encode_plus(
            text,
            None,
            add_special_tokens=True,
            truncation=True,
        )

        ort_inputs = {
            "ids": np.expand_dims(inputs["input_ids"], 0),
            "mask": np.expand_dims(inputs["attention_mask"], 0),
        }

        prediction = self.session.run(None, ort_inputs)

        return np_softmax(prediction)
