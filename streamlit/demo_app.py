from os import read
import streamlit as st
import pandas as pd
import numpy as np
import sys 
sys.path.append("./")
# 自作のやつら
from pytorch_utils import OnnxPredictor
from goo_lab.goo_apis import Goo

uploaded_file = st.file_uploader("ファイルアップロード", type='csv')

def load_model(model_path:str = "./onnx_model/epoch=9-valid_loss=0.1356-valid_acc=0.9745_quant.onnx"):
    predictor = OnnxPredictor(model_path=model_path, device="cpu")
    return predictor

model = load_model()

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    l = []
    for text in df["tweet"]:
        # st.write(text)
        # st.write(np.argmax(model.predict(text)[0][0]))
        score = model.predict(text)[0][0][1]
        l.append(score)
        # st.write(score)
    df["score"] = l
    st.write(df.query("score > 0.9")[["username", "tweet", "score"]])
    st.write(df.query("score <= 0.9")[["username", "tweet", "score"]])


    app_id = "e8be92a5e7fbf6a4b60bb8ff34cbdbf551e65a626b32090fe095864a7f2565e3"
    st.write(df["tweet"][0])
    st.write(df["tweet"][1])
    st.write(Goo(app_id=app_id, request_id="record001").textpair(text1=df["tweet"][0], text2=df["tweet"][1]).text)
