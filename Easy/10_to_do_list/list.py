#Challenge 10 - Easy
#this helps with learning tkinter GUI

#create GUI elements
from tkinter import *  
import random

#create event window

window = Tk()
 
window.title("Opening a window")
 
lbl = Label(window, text="Hello", font=("Arial Bold", 50))

 
lbl.grid(column=0, row=0)


#start main event loop
window.mainloop()
