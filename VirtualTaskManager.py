from tkinter import *
from gtts import gTTS
import pygame as pg
import speech_recognition as sr
import os 
r = sr.Recognizer()

count = 1
f = open('./test.txt', 'r')
text  = str(f.read())
f.close()
for i in text:
    if i == "\n":
        count += 1

def speakFile():
    f = open('./test.txt', 'r')
    text  = str(f.read())
    f.close() 
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

    # waiting for completing the audio
    while pg.mixer.music.get_busy():
        continue

    # exiting the pygame to delete the audio file
    pg.mixer.music.stop()
    pg.mixer.quit()
    os.remove("voice.mp3")


def listen():
    global count
    with sr.Microphone() as source:
        print("Say Something")
        audio = r.listen(source)
        print("Done")
    try:
        text = r.recognize_google(audio)
        print("You said: " + text)
        text += "\n"
        f = open('./test.txt', 'a')
        f.write("Task " + str(count) + ": " + text)
        count += 1
        f.close()
    except Exception as e:
        print("I was not able to understad please repeat")
        print(e)















root = Tk()
root.geometry("140x120")
myLabel = Label(root, text="I am your small agent")
myLabel.pack()

myButton1 = Button(root, text="Tell Me", bg="red", command=speakFile)
myButton1.config(height=2, width=10)
myButton2 = Button(root, text="Listen", bg="blue",command=listen)
myButton2.config(height=2, width=10)
myButton1.pack()
myButton2.pack()
root.mainloop()
