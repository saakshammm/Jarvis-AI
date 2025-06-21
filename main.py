import speech_recognition as sr
import win32com.client
import webbrowser
import os
import datetime
import requests
from config import apikey

# for TTS
speaker = win32com.client.Dispatch("SAPI.SpVoice")

def ai(prompt):
    API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"
    headers = {"Authorization": f"Bearer {apikey}"}

    payload = {
        "inputs": f"<|system|>You are a helpful assistant.<|end|><|user|>{prompt}<|end|><|assistant|>",
        "parameters": {
            "temperature": 0.7,
            "max_new_tokens": 200,
            "return_full_text": True
        }
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        data = response.json()
        if isinstance(data, list) and "generated_text" in data[0]:
            reply = data[0]["generated_text"]
            cleaned = reply.split("<|assistant|>")[-1].strip()
            print(cleaned)
            return cleaned
        else:
            print("Unexpected response format:", data)
            return "AI responded in an unexpected format."
    else:
        print("API Error:", response.status_code)
        return "Sorry, I couldn't get a valid response from AI."


def say(s): # a function for tts
    print("[Jarvis Speaking]")
    speaker.Speak(s)


def takeCommand(): # inputs what u said
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("[Jarvis Listening...]")
        audio = r.listen(source)
        print("[Jarvis Got Audio]")

    try:
        print("[Recognising]")
        query = r.recognize_google(audio, language="en-in")
        print(f"[You]: {query}")
        return query
    except Exception as e:
        return "Some error occurred. Sorry from Jarvis."


if __name__ == "__main__":
    say("Jarvis AI.")
    while True:
        query = takeCommand()
        # say(text)
        sites = [["youtube", "https://youtube.com"], ["wikipedia", "https://wikipedia.com"], ["google", "https://google.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]}..")
                webbrowser.open(site[1])

        # for time
        if "the time" in query.lower():
            dTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"The time is {dTime}")

        elif "open spotify" in query.lower():
            folderPath = r"C:\Users\saaks\AppData\Roaming\Spotify\Spotify.exe"
            if os.path.exists(folderPath):
                os.startfile(folderPath)
            else:
                print("[Jarvis] Folder not found.")

        elif "open discord".lower() in query.lower():
            folderPath = r"C:\Users\saaks\AppData\Local\Discord\Update.exe --processStart Discord.exe"
            if os.path.exists(folderPath):
                os.startfile(folderPath)
            else:
                print("[Jarvis] Folder not found.")
        elif "Using AI".lower() or "Using artificial intelligence".lower() in query:
            answer = ai(prompt=query)
            say(answer)
        else:
            answer = ai(prompt = query)
            say(answer)
