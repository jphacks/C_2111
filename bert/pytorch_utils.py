import numpy as np
import os 
import onnxruntime
from transformers import DistilBertTokenizer
import numpy as np
import json
import os
import re
import emoji
import mojimoji
import neologdn


emoji_json_path = "emoji/emoji_ja.json"
json_open = open(emoji_json_path)
emoji_dict = json.load(json_open)


def clean_sentence(sentence: str) -> str:
    """
    Bertに入れる前にtextに行う前処理

    Args:
        sentence (str): [description]

    Returns:
        str: [description]
    """
    sentence = re.sub(r"<[^>]*?>", "", sentence)  # タグ除外
    sentence = mojimoji.zen_to_han(sentence, kana=False)
    sentence = neologdn.normalize(sentence)
    sentence = re.sub(
        r'[!"#$%&\'\\\\()*+,\-./:;<=>?@\[\]\^\_\`{|}~「」〔〕“”〈〉『』【】＆＊・（）＄＃＠？！｀＋￥％︰-＠]。、♪',
        " ",
        sentence,
    )  # 記号
    sentence = re.sub(r"https?://[\w/:%#\$&\?\(\)~\.=\+\-]+", "", sentence)
    sentence = sentence.replace("'🏻'", " ")
    sentence = re.sub(r"[0-9０-９a-zA-Zａ-ｚＡ-Ｚ]+", "", sentence) # " "にしたほうがいいかも
    sentence = "".join(
        [
            "絵文字" + emoji_dict.get(c, {"short_name": ""}).get("short_name", "")
            if c in emoji.UNICODE_EMOJI["en"]
            else c
            for c in sentence
        ]
    )

    return sentence


def np_softmax(x):
    exp_x = np.exp(x)
    return exp_x / np.sum(exp_x)

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
