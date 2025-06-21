# 🧠 Jarvis AI – Voice-Activated Desktop Assistant

Jarvis AI is a Python-based voice assistant that listens to your commands, thinks using Hugging Face AI, and talks back like a real assistant.

## 🚀 Features

- 🎙️ Voice input (speech recognition)
- 🧠 Smart replies using Hugging Face `zephyr-7b-beta`
- 🔊 Speaks responses using Windows TTS
- 🌐 Opens websites (YouTube, Google, Wikipedia)
- 📂 Opens apps like Spotify and Discord (if installed)
- 🕒 Tells current time
- 💬 Answers anything else using AI

## 🛠️ How to Set Up

1. Clone the repo or download the files.
2. Install dependencies:
3. Create a `config.py` file in the project folder:
```python
apikey = "hf_your_huggingface_token_here"
```
4. python main.py


📝 Example Commands
“Open YouTube”
“What’s the time?”
“Who is Elon Musk?”
“Tell me a joke”
“What is a black hole?”


# 📦 Requirements
nginx
Copy
Edit
speechrecognition
requests
pywin32

# 🤖 Powered by
Hugging Face Zephyr 7B: https://huggingface.co/HuggingFaceH4/zephyr-7b-beta

Python + Windows TTS
