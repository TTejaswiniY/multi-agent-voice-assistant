import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

def speak(text, agent='realist'):
    if agent == 'realist':
        engine.setProperty('voice', voices[0].id)
    elif agent == 'expert':
        engine.setProperty('voice', voices[2].id)  # or index 1, based on your system
    else:
        engine.setProperty('voice', voices[0].id)
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        query = recognizer.recognize_google(audio)
        print("User said:", query)
        return query
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
        return ""
    except sr.RequestError:
        print("Could not request results.")
        return ""
