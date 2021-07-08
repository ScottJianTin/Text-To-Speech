from tkinter import *
from gtts import gTTS
from playsound import playsound

# Initialize tkinter


root = Tk()
root.geometry("350x300")
root.configure(bg="ghost white")
root.title("Text to Speech")

# Define variables


msg = StringVar()

# Header & Footer


Label(root, text="TEXT TO SPEECH",
      font="arial 20 bold", bg="white smoke").pack()
Label(root, text="~ Google Text To Speech ~",
      font="arial 15 bold", bg="white smoke", width="20").pack(side=BOTTOM)

# Text input


Label(root, text="Enter text: ", font="arial 15 bold",
      bg="white smoke").place(x=20, y=60)
entry_field = Entry(root, textvariable=msg, width="50")
entry_field.place(x=20, y=100)


# Define convert text to speech  function


def text_to_speech():
    message = entry_field.get()
    speech = gTTS(text=message)
    speech.save("textToSpeech.mp3")
    playsound("textToSpeech.mp3")

# Define exit function


def exit():
    root.destroy()

# Define reset function


def reset():
    msg.set("")


# Buttons


Button(root, text="PLAY", font="arial 13 bold",
       command=text_to_speech, width="6").place(x=25, y=140)
Button(root, text="RESET", font="arial 13 bold",
       command=reset, width="6", bg="LimeGreen").place(x=135, y=140)
Button(root, text="EXIT", font="arial 13 bold",
       command=exit, width="6", bg="OrangeRed").place(x=235, y=140)

root.mainloop()
