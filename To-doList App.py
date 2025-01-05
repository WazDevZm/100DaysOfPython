import tkinter
from tkinter import *

# This is Wazingwa's To-Do List app being made using Python from scratch
box = Tk()
box.title("My To-do App")
box.geometry("400x650+400+100")
box.resizable(False, False)

task_list = []

# Top bar
heading = Label(box, text="All my tasks!", font="arial 20 bold", fg="black")
heading.place(x=100, y=20)

# Entry frame
frame = Frame(box, width=400, height=50, bg="white")
frame.place(x=0, y=80)

# Task entry field
task_entry = Entry(frame, width=18, font="arial 20", bd=0)
task_entry.place(x=10, y=7)
task_entry.focus()

# Add button
button = Button(frame, text="ADD", font="arial 20 bold", width=6, bg="#5a95ff", fg="#fff", bd=0)
button.place(x=300, y=0)

# Listbox frame
frame1 = Frame(box, bd=3, width=400, height=400, bg="#32405b")
frame1.place(x=0, y=150)

# Listbox
listbox = Listbox(frame1, font=('arial', 12), width=40, height=20, bg="#32405b", fg="white", cursor="hand2", selectbackground="#5a95ff")
listbox.pack(side=LEFT, fill=BOTH, padx=2)


scrollbar= Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)


listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)




#deleteTask
#Delete_icon = PhotoImage(file="Images/waz.png")
#Button(box, image=Delete_icon, bd=0).pack(side=BOTTOM, pady=13)
button1 = Button(box, text="Delete", font="arial 20 bold",bg="red", fg="#fff", bd=0)
button1.pack(side=BOTTOM, pady=13)

box.mainloop()
