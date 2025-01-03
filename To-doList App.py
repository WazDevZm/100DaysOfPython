import tkinter
from tkinter import *

#This is Wazingwa's To -Do List app being made using Python from scratch
box = Tk()
box.title("My To-do App")
box.geometry("400x650+400+100")
box.resizable(False, False)

task_list = []

#Image_icon = PhotoImage(file="Images/waz.png")
#box.iconphoto(False, Image_icon)

#top bar
heading = Label(box, text = "All my tasks!", font="arial 20 bold", fg="black")
heading.place(x=100, y= 20)



#main
frame =  Frame(box, width=400, height=50, bg="white")
frame.place(x=0, y=180)

#taskStringVar()
task_entry = Entry(frame, width = 18, font="arial 20", bd=0)
task_entry.place(x=10, y=7)
task_entry.focus()



button = Button(frame, text = "ADD", font = "arial 20 bold", width=6, bg="#5a95ff",fg="#fff", bd=0)
button.place(x=300, y=0)

#listbox
frame1= Frame(box, bd=3, width=700, height=280, bg="#32405b")
frame1.pack(pady=(160,0))


listbox =Listbox(frame1, font=('arial', 12), width=40, height=16, bg="#32405b")
listbox.pack(side=LEFT, fill=BOTH)










box.mainloop()