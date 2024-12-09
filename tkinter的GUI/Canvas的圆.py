from tkinter import *

win = Tk()
canvas = Canvas(win)
canvas.create_oval(13,13,240,240,fill="red",outline="blue")
canvas.pack()
win.mainloop()