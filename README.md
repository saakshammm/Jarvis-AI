<img src="A_2D_digital_graphic_design_banner_for_a_project_n.png" alt="Jarvis AI Banner" style="width:100%;"/>
# 🧠 Jarvis AI – Voice-Activated Desktop Assistant

Jarvis AI is a Python-based personal assistant that listens to your voice, thinks using Hugging Face AI, and talks back like a real human assistant.

## 🚀 Features

- 🎙️ Voice input using microphone
- 🤖 Smart replies powered by Hugging Face (`zephyr-7b-beta`)
- 🔊 Speaks responses using Windows TTS (Text-to-Speech)
- 🌐 Opens websites: YouTube, Google, Wikipedia
- 💻 Launches apps like Spotify and Discord
- 🕒 Tells current time
- 💬 Answers anything else using AI

## 🛠️ How to Set Up

1. Clone or download this repo
2. Install dependencies:
```

pip install -r requirements.txt

````
3. Create a `config.py` file in the project root with your Hugging Face API key:
```python
apikey = "hf_your_huggingface_token_here"
````

4. Run the assistant:

   ```
   python main.py
   ```

## 📝 Example Commands

* “Open YouTube”
* “What’s the time?”
* “Who is Elon Musk?”
* “Tell me a joke using AI”
* “What is a black hole?”

## 🔐 .gitignore Included

This repo already ignores:

```
config.py
.venv/
.idea/
__pycache__/
```

## 📦 Requirements

```
speechrecognition
requests
pywin32
```

## 🤖 Powered By

* [Hugging Face Zephyr 7B](https://huggingface.co/HuggingFaceH4/zephyr-7b-beta)
* Python 3.10+
* Windows built-in TTS engine
---

### 🛠️ Made with 💻 and ☕ by [Saksham](https://github.com/saakshammm)

