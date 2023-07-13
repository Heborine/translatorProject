from tkinter import *

from googletrans import Translator

import constants

# def periodic(periodic):
#     global window
#     translate_texts("hello")
#     window.after(10, periodic, periodic)

def task():
    # this is where everything happens
    global window
    translate_texts("hello")
    window.after(2000, task)


def translate_texts(text):
    global input_choice, output_choice
    translator = Translator()
    translation = translator.translate(text, src=input_choice.get(), dest=output_choice.get())
    print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
    print("The confidence was:", translation.extra_data["confidence"])


def start_window():
    global input_choice, output_choice, window
    window = Tk()
    window.title('Translator')
    window.geometry("800x800")
    window.config(background="lightgray")

    label_input = Label(window, text="Input Language", width=20, height=2, fg="blue")
    label_output = Label(window, text="Output Language", width=20, height=2, fg="blue")

    input_choice = StringVar(window)
    input_choice.set('english')
    input_option = OptionMenu(window, input_choice, *constants.languages)
    input_option.config(width=20, bg="gray")

    output_choice = StringVar(window)
    output_choice.set('english')
    output_option = OptionMenu(window, output_choice, *constants.languages)
    output_option.config(width=20, bg="gray")

    label_input.grid(column=1, row=1, pady=10)
    label_output.grid(column=2, row=1, pady=10)
    input_option.grid(column=1, row=2, pady=10)
    output_option.grid(column=2, row=2, pady=10)
    #periodic("hi")
    # window.bind('<Configure', translate_texts("hello"))
    window.after(2000, task)
    window.mainloop()


if __name__ == '__main__':
    start_window()
