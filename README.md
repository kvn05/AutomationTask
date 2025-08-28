# 🔊 Article / Document to Audio Converter

A powerful Streamlit web application that converts articles and documents into audio files using Google Text-to-Speech (gTTS). Perfect for creating podcasts, audiobooks, or accessibility solutions.

![Python](https://img.shields.io/badge/python-v3.7+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-latest-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## ✨ Features

- **🌐 Web Article Conversion**: Extract text from any web URL and convert to audio
- **📂 File Upload Support**: Upload PDF or TXT files for audio conversion
- **🎙️ Multi-language Support**: Convert text to speech in multiple languages (English, Hindi, Gujarati, French, German, Spanish)
- **⚙️ Customizable Settings**: 
  - Adjustable speech speed (normal/slow)
  - Configurable text chunking for large documents
- **📥 Easy Downloads**: Download individual audio segments
- **🎵 In-browser Playback**: Listen to audio directly in the web interface
- **📊 Progress Tracking**: Real-time conversion progress indicator

## 🚀 Demo

![Demo Screenshot](demo.png) <!-- Add your screenshot here -->

## 🛠️ Installation

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Quick Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/article-to-audio-converter.git
   cd article-to-audio-converter
   ```

2. **Install required dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Open your browser** and navigate to `http://localhost:8501`

## 📦 Dependencies

Create a `requirements.txt` file with the following:

```
streamlit>=1.28.0
requests>=2.31.0
beautifulsoup4>=4.12.0
gtts>=2.4.0
PyPDF2>=3.0.1
```

## 🎯 Usage

### Converting Web Articles

1. Select **"🌐 URL"** option
2. Enter the article URL in the input field
3. Click **"Fetch Article"** to extract text
4. Adjust voice settings in the sidebar if needed
5. Click **"Convert to Audio"** to generate audio files
6. Play audio in-browser or download individual segments

### Converting Documents

1. Select **"📂 Upload File"** option
2. Upload a PDF or TXT file using the file uploader
3. Preview the extracted text
4. Configure voice settings (language, speed, chunk length)
5. Click **"Convert to Audio"** to start conversion
6. Download or play the generated audio files

### Voice Settings

- **Language**: Choose from English, Hindi, Gujarati, French, German, or Spanish
- **Slow Speech**: Enable for slower, more deliberate speech
- **Chunk Length**: Adjust how text is split (1000-5000 characters per segment)

## 📁 Project Structure

```
article-to-audio-converter/
│
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── demo.png              # Screenshot (optional)
└── .gitignore           # Git ignore file
```

## 🔧 Configuration

### Adding More Languages

To add more languages, modify the language selectbox in the sidebar:

```python
language = st.sidebar.selectbox("Language", [
    "en",  # English
    "hi",  # Hindi
    "gu",  # Gujarati
    "fr",  # French
    "de",  # German
    "es",  # Spanish
    "ja",  # Japanese
    "ko",  # Korean
    # Add more language codes as needed
])
```

### Customizing Chunk Sizes

Adjust the chunk length slider range:

```python
chunk_length = st.sidebar.slider("Split text every N characters:", 500, 10000, 2500)
```

## 🐛 Troubleshooting

### Common Issues

**Error: "No module named 'streamlit'"**
```bash
pip install streamlit
```

**Error: "Could not extract text from PDF"**
- Ensure the PDF contains selectable text (not scanned images)
- Try with a different PDF file

**Error: "No text found on this page"**
- The webpage might be using JavaScript to load content
- Try a different URL or check if the page loads properly

**Audio not playing**
- Check your browser's audio settings
- Try downloading the file and playing it locally

### Performance Tips

- For large documents, increase chunk length to reduce the number of audio files
- Use slower speech settings for better pronunciation of technical terms
- Close other browser tabs to improve performance during conversion

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Ideas for Contributions

- Add support for more file formats (DOCX, EPUB)
- Implement voice selection (different TTS voices)
- Add batch processing capabilities
- Create audio merging functionality
- Improve web scraping for complex websites
- Add support for more languages

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Streamlit](https://streamlit.io/) for the amazing web framework
- [gTTS](https://github.com/pndurette/gTTS) for Google Text-to-Speech integration
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) for web scraping
- [PyPDF2](https://github.com/py-pdf/PyPDF2) for PDF text extraction

## 📞 Support

If you encounter any issues or have questions:

- Create an issue on GitHub
- Contact: your.email@example.com
- Documentation: [Wiki](https://github.com/yourusername/article-to-audio-converter/wiki)

## 🗺️ Roadmap

- [ ] Add support for DOCX files
- [ ] Implement voice customization options
- [ ] Add batch processing for multiple URLs
- [ ] Create mobile-responsive design
- [ ] Add audio merging functionality
- [ ] Implement user accounts and history
- [ ] Add support for custom TTS services

---

⭐ If you found this project helpful, please give it a star on GitHub!

Made with ❤️ using Streamlit and gTTS
