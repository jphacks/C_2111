from os import read
import streamlit as st
from pytorch_utils import OnnxPredictor
import pandas as pd
import numpy as np

uploaded_file = st.file_uploader("ファイルアップロード", type='csv')

def load_model(model_path:str = "./onnx_model/epoch=9-valid_loss=0.6320-valid_acc=1.0000_quant.onnx"):
    predictor = OnnxPredictor(model_path=model_path, device="cpu")
    return predictor

model = load_model()

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    for text in df["tweet"]:
        df["score"] = model.predict(text)[0][0][0]
    
    st.write(df)


