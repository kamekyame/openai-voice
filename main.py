import io
import streamlit as st
from openai import OpenAI

import openai

client = OpenAI()
openai.api_key = st.secrets["OPENAI_API_KEY"]

def stream_and_play(text):
    response = client.audio.speech.create(
        model="tts-1",
        voice="nova",
        input=text,
    )
    
    # OpenAI APIのレスポンスから直接バイナリコンテンツを使用
    audio_bytes = response.content
    return audio_bytes

# Streamlitウィジェットのセットアップ
if __name__ == "__main__":
    st.title("😱テキストから音声へ")
    text = st.text_area("テキストを入力してください:",height=300)
    if st.button("再生"):
        audio_bytes = stream_and_play(text)
        st.audio(audio_bytes, format='audio/mp3')