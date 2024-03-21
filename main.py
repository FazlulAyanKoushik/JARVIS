import speech_recognition as sr
import wikipedia
import openai
import pyttsx3
import os

"""
This is the main file for the project. In this project I build a JARVIS like assistant using python.
I an using speech_recognition library to convert speech to text and wikipedia library to get information from wikipedia.
I am also using openai library to get information from openai.
"""


class JARVIS:

    def say(self, text):
        """
        This function takes a string as input and speaks it using pyttsx3 library.
        """
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

    def listen(self):
        """
        This function listens to the user and converts the speech to text.
        """
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            # audio = recognizer.adjust_for_ambient_noise(source, duration=1)  # adjust for ambient noise
            audio = r.listen(source)  # listen to the source
            try:
                text = r.recognize_google(audio)
                print("You said: " + text)
                return text
            except Exception as e:
                print(e)
                return "Sorry, I could not understand you."


if __name__ == '__main__':
    jarvis = JARVIS()

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You said: " + text)
        except:
            text = ""

        if text and text.lower() == "hey jarvis":
            jarvis.say("Hello, I am JARVIS. How can I help you?")
            text = jarvis.listen()
            jarvis.say("You said: " + text)
        else:
            jarvis.say("I cant here you")
