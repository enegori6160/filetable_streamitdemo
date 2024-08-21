import streamlit as st
import pandas as pd

# CSVファイルのアップロード
uploaded_file = st.file_uploader("CSVファイルをアップロードしてください", type=["csv"])

# アップロードされたファイルをデータフレームに読み込む
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # テーブルの表示
    st.write("### アップロードされたテーブル")
    st.write(df)
