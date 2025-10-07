import streamlit as st
from PIL import Image 

st.title("タイトルです")
st.caption("これはテスト用のキャプションです")

image = Image.open("./data/モンハンワイルズ_ベンチマーク.jpg") # 相対パスを指定
st.image(image,width=200)