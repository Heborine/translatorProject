# import speech_recognition as sr
# import pyttsx3
#
# r = sr.Recognizer()
#
# def SpeakText(command):
#     engine = pyttsx3.init()
#     engine.say(command)
#     engine.runAndWait()
#
# while(1):
#     try:
#         with sr.Microphone() as source2:
#             r.adjust_for_ambient_noise(source2, duration=0.2)
#             audio2 = r.listen(source2)
#             MyText = r.recognize_google(audio2)
#             MyText = MyText.lower()
#             print(MyText)
#             # SpeakText(MyText)
#     except sr.RequestError as e:
#         print(e)
#     except sr.UnknownValueError:
#         print("Unknown")

# import speech_recognition as sr
# import pyaudio
#
# init_rec = sr.Recognizer()
# print("Let's speak!!")
# with sr.Microphone() as source:
#     audio_data = init_rec.listen(source)
#     print("Recognizing your text.............")
#     text = init_rec.recognize_google(audio_data)
#     print(text)

# import speech_recognition as sr
# import os
# from pocketsphinx import LiveSpeech, get_model_path
#
# # obtain audio from the microphone
# r = sr.Recognizer()
# with sr.Microphone() as source:
#     print("Please wait. Calibrating microphone...")
#     # listen for 5 seconds and create the ambient noise energy level
#     r.adjust_for_ambient_noise(source, duration=5)
#     print("Say something!")
#     audio = r.listen(source)
#
#     # recognize speech using Sphinx
#     try:
#         print("Sphinx thinks you said '" + r.recognize_sphinx(audio) + "'")
#     except sr.UnknownValueError:
#         print("Sphinx could not understand audio")
#     except sr.RequestError as e:
#         print("Sphinx error; {0}".format(e))

# import speech_recognition as sr
# r = sr.Recognizer()
# while True:
#     with sr.Microphone() as source:
#         try:
#             r.adjust_for_ambient_noise(source, duration=1)
#         # read the audio data from the default microphone
#         # convert speech to text
#             text = r.recognize_google(r.listen(source))
#             print(text)
#         except:
#             print("")

import speech_recognition as sr
import pyaudio

init_rec = sr.Recognizer()
print("Let's speak!!")
while True:
    with sr.Microphone() as source:
        try:
            audio_data = init_rec.record(source, duration=2)
            print("Recognizing your text.............")
            text = init_rec.recognize_google(audio_data)
            print(text)
        except:
            print("/")