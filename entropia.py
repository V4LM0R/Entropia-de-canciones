import streamlit as st
import numpy as np
from collections import Counter

def calculate_entropy(text):
    freq = Counter(text)
    freqs = np.array(list(freq.values()))
    probs = freqs / sum(freqs)
    ent = -np.sum(probs * np.log2(probs))
    return ent

st.title("Calculadora de Entropía para Canciones")

uploaded_file = st.file_uploader("Sube un archivo de texto con la letra de la canción", type="txt")

if uploaded_file is not None:
    song_lyrics = uploaded_file.read().decode("utf-8")
    st.text_area("Letra de canción :", song_lyrics, height=200)
    ent = calculate_entropy(song_lyrics)
    st.write(f"La entropía de la canción es: {ent:.4f}")
