# app.py
import streamlit as st

st.title("はじめてのWebアプリ")

name = st.text_input("名前を入力")

if name:
    t       .success(f"こんにちは、{name} さん！")

    age = st.slider("年齢", 0, 100, 25)
    st.write(f"あなたは{age}歳ですね")
