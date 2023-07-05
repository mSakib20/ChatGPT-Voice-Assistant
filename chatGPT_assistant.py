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
    
    # Format the user's input and append it to the conversation history
    prompt = f"{userName}: {userInput}\n{aiName}:"
    conversation += prompt

    # Used the OpenAI API to generate a response based on the conversation
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=conversation,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Extract the AI's response text from the API's response and strip leading/trailing whitespace
    responseText = response.choices[0].text.strip()
    
    # Append the AI's response to the conversation history and print it
    conversation += responseText + "\n"
    conversation += responseText + "\n"
    print(responseText)

    # Speak the AI's response
    engine.say(responseText)
    engine.runAndWait()
