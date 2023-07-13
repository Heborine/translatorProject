# from tkinter import *
# import threading
#
# import constants
#
#
# class App(threading.Thread):
#     def __init__(self):
#         threading.Thread.__init__(self)
#         self.start()
#         self.window = Tk()
#
#     def callback(self):
#         self.window.quit()
#
#     def start_window(self):
#         global input_choice, output_choice, window  # , r
#
#         # a = pyttsx3.init("sapi5", False)
#         # a.say("Hi")
#         # a.runAndWait()
#         # r = sr.Recognizer()
#
#         # self.window = Tk()
#         self.window.title('Translator')
#         self.window.iconphoto(True, PhotoImage(file='misc\\icon.gif'))
#         self.window.geometry("385x300")
#         self.window.config(background="lightgray")
#
#         self.window.protocol("WM_DELETE_WINDOW", self.callback)
#
#         label_input = Label(self.window, text="Input Language", width=20, height=2, fg="blue")
#         label_output = Label(self.window, text="Output Language", width=20, height=2, fg="blue")
#
#         input_choice = StringVar(self.window)
#         input_choice.set('English')
#         input_option = OptionMenu(self.window, input_choice, *constants.languages)
#         input_option.config(width=20, bg="gray")
#
#         output_choice = StringVar(self.window)
#         output_choice.set('English')
#         output_option = OptionMenu(self.window, output_choice, *constants.languages)
#         output_option.config(width=20, bg="gray")
#
#         button_exit = Button(self.window,
#                              text="Exit",
#                              command=exit,
#                              fg="darkgreen",
#                              width=5,
#                              bg="lightgray",
#                              pady=0,
#                              font=("Helvetica", 10))
#
#         label_input.grid(column=1, row=1, pady=10)
#         label_output.grid(column=3, row=1, pady=10)
#         input_option.grid(column=1, row=2, pady=10)
#         output_option.grid(column=3, row=2, pady=10)
#         button_exit.grid(column=2, row=3)
#         # window.after(2000, task)
#         self.window.mainloop()
#
# if __name__ == '__main__':
#     app = App()
#     app.start_window()
#     for i in range(10000):
#         print(i)
# Run tkinter code in another thread

import tkinter as tk
import threading

import constants


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
                                command=exit,
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

if __name__ == '__main__':
    app = App()
    for i in range(10000):
        print(i)