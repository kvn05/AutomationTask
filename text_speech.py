import streamlit as st
import requests
from bs4 import BeautifulSoup
from gtts import gTTS
import tempfile
import os
import time
from PyPDF2 import PdfReader

st.set_page_config(page_title="Article to Audio", page_icon="🔊", layout="wide")
st.title("🔊 Article / Document to Audio Converter (gTTS)")

# Input type selection
option = st.radio("Select Input Type:", ["🌐 URL", "📂 Upload File"])

text = ""
title = ""

if option == "🌐 URL":
    url = st.text_input("Enter the article URL:")
    if st.button("Fetch Article"):
        if not url.strip():
            st.error("❌ Please enter a valid URL.")
        else:
            try:
                response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
                soup = BeautifulSoup(response.text, "html.parser")
                title = soup.find("title").get_text() if soup.find("title") else "Untitled Article"
                text = " ".join([p.get_text() for p in soup.find_all("p")])

                if not text.strip():
                    st.warning("⚠️ No text found on this page.")
                else:
                    st.success("✅ Article fetched successfully!")
                    st.subheader(f"📖 {title}")
                    st.write(text[:500] + "...")  # Preview
            except Exception as e:
                st.error(f"Error fetching article: {e}")

elif option == "📂 Upload File":
    uploaded_file = st.file_uploader("Upload a PDF or TXT file", type=["pdf", "txt"])
    if uploaded_file:
        try:
            if uploaded_file.type == "application/pdf":
                reader = PdfReader(uploaded_file)
                text = " ".join([page.extract_text() for page in reader.pages if page.extract_text()])
                title = uploaded_file.name
            elif uploaded_file.type == "text/plain":
                text = uploaded_file.read().decode("utf-8")
                title = uploaded_file.name

            if not text.strip():
                st.warning("⚠️ Could not extract any text from this file.")
            else:
                st.success("✅ File loaded successfully!")
                st.subheader(f"📄 {title}")
                st.write(text[:500] + "...")  # Preview
        except Exception as e:
            st.error(f"Error reading file: {e}")

# Sidebar settings
st.sidebar.header("🎙️ Voice Settings")
language = st.sidebar.selectbox("Language", ["en", "hi", "gu", "fr", "de", "es"])  # More can be added
slow = st.sidebar.checkbox("Slow Speech", value=False)
chunk_length = st.sidebar.slider("Split text every N characters:", 1000, 5000, 2500)

# Convert button
if text.strip() and st.button("Convert to Audio"):
    try:
        chunks = [text[i:i+chunk_length] for i in range(0, len(text), chunk_length)]
        audio_files = []

        progress = st.progress(0)
        for idx, chunk in enumerate(chunks, start=1):
            tts = gTTS(text=chunk, lang=language, slow=slow)
            tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix=f"_{idx}.mp3")
            tts.save(tmp_file.name)
            tmp_file.close()
            audio_files.append(tmp_file.name)
            progress.progress(idx / len(chunks))
            time.sleep(0.1)

        st.success("✅ Conversion successful!")

        # Display audio players + download buttons
        for idx, audio_file in enumerate(audio_files, start=1):
            st.audio(audio_file, format="audio/mp3")
            with open(audio_file, "rb") as f:
                st.download_button(
                    label=f"Download Part {idx}",
                    data=f,
                    file_name=f"{title}_part_{idx}.mp3",
                    mime="audio/mp3"
                )

    except Exception as e:
        st.error(f"Something went wrong: {e}")
