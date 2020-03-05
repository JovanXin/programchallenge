#Challenge 10 - Easy
#this helps with learning tkinter GUI

#create GUI elements
import tkinter as tk
import random

#create event window

root = tk.Tk()

#creates a button

button = tk.Button(root, text="test button", bg='grey')
button.pack()
#start main event loop
root.mainloop()