from tkinter import *

win = Tk()
coord = 13,50,240,213
canvas = Canvas(win)
canvas.create_arc(coord,start=0,extent=270,fill="red")
canvas.pack()
win.mainloop()