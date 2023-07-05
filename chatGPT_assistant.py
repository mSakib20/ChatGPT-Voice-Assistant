# Importing the libraries for speech recognition, pyttsx3, and openAI
import speech_recognition as sr
import pyttsx3
import openai

# Setting up the openAI API key
openai.api_key = "USE YOUR API"

# Setting up the speech recognition engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # voices[1] = male voice

recognizer = sr.Recognizer()
microphone = sr.Microphone(device_index=1)

# Setting up the conversation variables
conversation = ""
userName = "User"
aiName = "chatGPT"

# Setting up the conversation loop
while True:
    with microphone as source:
        print("Say something!")
        recognizer.adjust_for_ambient_noise(source, duration=0.2)
        audio = recognizer.listen(source)
        print("Got it!")
    print("Processing...")

    # Converting the audio to text
    try:
        userInput = recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        continue