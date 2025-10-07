import streamlit as st
import pandas as pd
#df = pd.read_csv('平均気温.csv',index_col='月')
# st.dataframe(df)
# st.table(df) 画面いっぱいに表示
# st.line_chart(df) 折れ線グラフ
# st.bar_chart(df['2025年']) 棒グラフ

video_file = open('./data/file_25-10-02_13-24-44.mp4','rb')
video_bytes = video_file.read()
st.video(video_bytes)