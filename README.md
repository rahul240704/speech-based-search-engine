# speech-based-search-engine


---

## 🗣️ Speech-Based Search Engine

This Python script is a simple **voice-activated web search tool**. It allows users to speak a search query into their microphone, which the script then converts into text using speech recognition, and opens the relevant Google search results in a web browser.

### 🔧 Features

* Captures user voice input via microphone
* Converts speech to text using Google Web Speech API
* Opens a Google search for the recognized query
* Uses text-to-speech (TTS) to interact with the user

---

### 📦 Requirements

Install the required packages with:

```bash
pip install SpeechRecognition pyttsx3 pyaudio
```

> Note: `pyaudio` can be tricky to install. For Windows, use:
>
> ```bash
> pip install pipwin
> pipwin install pyaudio
> ```

---

### 🚀 How to Run

```bash
python "speech based search engine (2).py"
```

Make sure your microphone is connected and working.

---

### 🧠 How It Works

1. Greets the user and asks what they want to search for.
2. Listens to the spoken input.
3. Translates it into text using Google's Speech Recognition API.
4. Launches the search in your default web browser.
5. Reads back the search query.

---

### 🛑 Error Handling

* If speech is not recognized or there's a connectivity issue with the recognition service, the script provides feedback via TTS and exits gracefully.

---

