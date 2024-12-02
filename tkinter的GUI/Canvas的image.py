from tkinter import *

win = Tk()
img = PhotoImage(file="虎视眈眈.gif")
canvas = Canvas(win)
canvas.create_image(220,180,image=img)
canvas.pack()
win.mainloop()