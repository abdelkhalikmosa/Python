# pip install SpeechRecognition
# pip install pyttsx3
# pip install PyAudio
# pip install pywhatkit
# pip install wikipedia
# pip install pyjokes

from socket import socket

import speech_recognition as sr
import pyttsx3 as tts
import pywhatkit
import wikipedia
import pyjokes as jokes
import datetime

listener = sr.Recognizer()
engine = tts.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


# engine.say('Hey, I am your new assistant. How may I help you?')
# engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('I am listening to you now ....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
    except:
        pass
    return command


def run_assistant():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        talk('Playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'wikipedia' in command:
        info = wikipedia.summary(command, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        joke = jokes.get_joke()
        print(joke)
        talk(joke)


while True:
    run_assistant()
