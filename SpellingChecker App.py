import tkinter
from tkinter import *
from textblob import TextBlob


root = Tk()
root.title("Wazingwa's Spelling Checker")
root.geometry("700x400")
root.config(background="grey")

heading = Label(root, text="Wazingwa's Spelling Checker", font=("Trebuchet MS", 20, "bold"), bg="#dae6f6", fg="#364971")
heading.pack(pady=(50))


root.mainloop()