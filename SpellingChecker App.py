import tkinter
from tkinter import *
from textblob import TextBlob


root = Tk()
root.title("Wazingwa's Spelling Checker")
root.geometry("700x400")
root.config(background="#dae6f6")


def chech_spelling():
    word=center_text.get()
    a= TextBlob(word)
    right = str(a.correct())
    
    cs = Label(root,text = "Corret text is: ", font=("poppins", 20), bg= "#dae6f6", fg= "#364971")
    cs.place(x=100, y= 250)
    spell.config(text=right)
    

heading = Label(root, text="Wazingwa's Spelling Checker", font=("Trebuchet MS", 20, "bold"), bg="#dae6f6", fg="#364971")
heading.pack(pady=(50,0))

center_text = Entry (root, justify="center", width=30, font=("poppins", 25), bg="white", border=2)
center_text.pack(pady=10)
center_text.focus()


button = Button(root, text ="Check", font = ("arial", 20, "bold"), fg="white", bg="red", command=chech_spelling)
button.pack()


spell= Label(root, font = ("poppins", 20), bg="#dae6f6", fg="#364971")
spell.place(x=350, y=250)

root.mainloop()