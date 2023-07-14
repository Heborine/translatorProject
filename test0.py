# thread audio and have one recognize words and start print captioning while other with the duration delay starts next words in a loop
import threading

import speech_recognition as sr
import pyaudio

import time

def voice():
    # global source, init_rec
    global which
    which = 1
    init_rec = sr.Recognizer()
    print("Let's speak!!")
    with sr.Microphone() as source:
         try:
             t1 = threading.Thread(target=record_analyze, args=(source, init_rec))
             t1.start()
             t1.join
             t2 = threading.Thread(target=record_analyze2(source, init_rec))
             # t2 = threading.Thread(target=record_analyze2, args=(source, init_rec))
             t2.start()
             t2.join
             # audio_data = init_rec.record(source, duration=5)
             # print("Recognizing your text.............")
             # text = init_rec.recognize_google(audio_data)
             # print(text)
         except:
             print("/")


def record_analyze(source, init_rec):
    global which
    while True:
        try:
            if which == 1:
                print("Starting")
                audio_data = init_rec.record(source, duration=5)
                which = 2
                print("Recognizing your text.............")
                text = init_rec.recognize_google(audio_data)
                print(text)
            else:
                pass
        except:
            print("/")
        # time.sleep(4)
    # time.sleep(2)


def record_analyze2(source, init_rec):
    global which
    while True:
        # time.sleep(5)
        try:
            if which == 2:
                print("Starting")
                audio_data = init_rec.record(source, duration=5)
                which = 1
                print("Recognizing your text.............")
                text = init_rec.recognize_google(audio_data)
                print(text)
            else:
                pass
        except:
            print("/")

# def voice2():
#     # print("hi")
#     init_rec = sr.Recognizer()
#     print("Let's speak!!")
#     with sr.Microphone() as source2:
#         print('hi')
    #      try:
    #          audio_data = init_rec.record(source2, duration=5)
    #          print("Recognizing your text.............")
    #          text = init_rec.recognize_google(audio_data)
    #          print(text)
    #      except:
    #          print("/")


# t1 = threading.Thread(target=voice)
# t2 = threading.Thread(target=voice2)
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()
# while True:
voice()