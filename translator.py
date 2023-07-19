import tkinter as tk
import threading

import constants

import speech_recognition as sr
import pyaudio

# import sys
import os

from googletrans import Translator

class App(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.window = None
        self.start()

    def callback(self):
        self.window.quit()

    def run(self):
        global input_choice, output_choice, window
        self.window = tk.Tk()
        self.window.protocol("WM_DELETE_WINDOW", self.callback)

        self.window.title('Translator')
        self.window.iconphoto(True, tk.PhotoImage(file='misc\\icon.gif'))
        self.window.geometry("385x300")
        self.window.config(background="lightgray")

        label_input = tk.Label(self.window, text="Input Language", width=20, height=2, fg="blue")
        label_output = tk.Label(self.window, text="Output Language", width=20, height=2, fg="blue")

        input_choice = tk.StringVar(self.window)
        input_choice.set('English')
        input_option = tk.OptionMenu(self.window, input_choice, *constants.languages)
        input_option.config(width=20, bg="gray")

        output_choice = tk.StringVar(self.window)
        output_choice.set('English')
        output_option = tk.OptionMenu(self.window, output_choice, *constants.languages)
        output_option.config(width=20, bg="gray")

        button_exit = tk.Button(self.window,
                                text="Exit",
                                command=osexit,
                                fg="darkgreen",
                                width=5,
                                bg="lightgray",
                                pady=0,
                                font=("Helvetica", 10))

        label_input.grid(column=1, row=1, pady=10)
        label_output.grid(column=3, row=1, pady=10)
        input_option.grid(column=1, row=2, pady=10)
        output_option.grid(column=3, row=2, pady=10)
        button_exit.grid(column=2, row=3)

        # label = tk.Label(self.window, text="Hello World")
        # label.pack()

        self.window.mainloop()

def voice():
    # global source, init_rec
    global which, text
    which = 1
    text = ""
    init_rec = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            # t3 = threading.Thread(target=dictate)
            # t3.start()
            # t3.join()
            init_rec.adjust_for_ambient_noise(source, duration=5)
            # print("Let's speak!!")
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
            # dictate(text)
            # t3 = threading.Thread(target=dictate)
            # t3.start()
            # t3.join()
        except:
            # print("/")
            pass


def record_analyze(source, init_rec):
    global which, text
    while True:
        try:
            if which == 1:
                print("Starting")
                audio_data = init_rec.record(source, duration=5)
                which = 2
                # print("Recognizing your text.............")
                text = init_rec.recognize_google(audio_data)
                # print(text)
                dictate(text)
            else:
                pass
                # print("//")
                # text = ""
        except:
            pass
            # print("/")
            # text = ""
        # time.sleep(4)
    # time.sleep(2)


def record_analyze2(source, init_rec):
    global which, text
    while True:
        # time.sleep(5)
        try:
            if which == 2:
                print("Starting 2")
                audio_data = init_rec.record(source, duration=5)
                which = 1
                # print("Recognizing your text.............")
                text = init_rec.recognize_google(audio_data)
                # print(text)
                dictate(text)
            else:
                pass
                # print("//")
                # text = ""
        except:
            # print("/")
            # text = ""
            pass


def dictate(text):
    # global text
    # while True:
    #     if text != "":
    text = translate_texts(text)
    print("\n" + text + "\n")


def osexit():
    os._exit(0)

def translate_texts(text):
    global input_choice, output_choice
    translator = Translator()
    translation = translator.translate(text, src=input_choice.get(), dest=output_choice.get())
    return translation.text


if __name__ == '__main__':
    app = App()
    # dictate()
    voice()
    # dictate()

    # dictate()
    # for i in range(10000):
    #     print(i)