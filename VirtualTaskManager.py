from tkinter import *
from gtts import gTTS
import pygame as pg

def speakFile():
    f = open('./test.txt', 'r')
    text  = str(f.read())
    f.close() # I havve to look this also

    strText = ""

    for i in text:
        if i == "\n":
            strText += " "
        strText += i
    speak(strText)

def speak(text):
    obj = gTTS(text=text, lang="en", slow=False)
    obj.save("voice.mp3")
    pg.mixer.init()
    pg.mixer.music.load("voice.mp3")
    pg.mixer.music.play()
    

root = Tk()
root.geometry("140x120")
myLabel = Label(root, text="I am your small agent")
myLabel.pack()

myButton1 = Button(root, text="Tell Me", bg="red", command=speakFile)
myButton1.config(height=2, width=10)
myButton2 = Button(root, text="Listen", bg="blue")
myButton2.config(height=2, width=10)
myButton1.pack()
myButton2.pack()
root.mainloop()
