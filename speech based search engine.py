import speech_recognition as sr
import pyttsx3
import webbrowser

# Initialize the speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("What do you want to search for?")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"You said: {query}")
        return query
    except sr.UnknownValueError:
        speak("Sorry, I did not catch that.")
        return ""
    except sr.RequestError:
        speak("Sorry, there was a problem with the speech recognition service.")
        return ""

def search_web(query):
    if query:
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)
        speak(f"Here are the search results for {query}")
    else:
        speak("No search query provided.")

# Main function
if __name__ == "__main__":
    query = take_command()
    search_web(query)
