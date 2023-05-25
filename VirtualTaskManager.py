from tkinter import *

root = Tk()
root.geometry("140x120")
myLabel = Label(root, text="I am your small agent")
myLabel.pack()

myButton1 = Button(root, text="Tell Me", bg="red")
myButton1.config(height=2, width=10)
myButton2 = Button(root, text="Listen", bg="blue")
myButton2.config(height=2, width=10)
myButton1.pack()
myButton2.pack()
root.mainloop()
