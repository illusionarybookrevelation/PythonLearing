from tkinter import *

win = Tk()
canvas = Canvas(win)
canvas.create_line(13,13,40,120,230,270,width=3,fill="green")
canvas.pack()

win.mainloop()
