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
frame =  Frame(box, width=400, height=50, bg="grey")
frame.place(x=0, y=180)

#taskStringVar()
task_entry = Entry(frame, width = 18, font="arial 20", bd=0)
task_entry.place(x=10, y=7)
box.mainloop()


button = Button(frame, text = "ADD", font = "arial 20 bold", width=6, bg="blue",fg="white", bd=0)
button.place(x=300, y=0)
