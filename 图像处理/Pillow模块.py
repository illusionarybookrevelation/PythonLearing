from tkinter import *
from PIL import Image,ImageTk

win = Tk()
win.title(string="图片交错")

width=800
height=800
screenwidth=win.winfo_screenwidth()
screenheight=win.winfo_screenheight()
geometry='%dx%d+%d+%d' % (width,height,(screenwidth - width) / 2,(screenheight - height) / 2)
win.geometry(geometry)

img_1 = Image.open("./Photo/派蒙-翻涌吧.jpeg")
img_2 = Image.open("./Photo/派蒙-降众天华.jpeg")
img_3 = Image.open("./Photo/派蒙-万叶之一刀.jpeg")
img_4 = Image.open("./Photo/派蒙-天街巡游.jpeg")

image_1 = ImageTk.PhotoImage(img_1)
image_2 = ImageTk.PhotoImage(img_2)
image_3 = ImageTk.PhotoImage(img_3)
image_4 = ImageTk.PhotoImage(img_4)

canvas = Canvas(win,width=800,height=800)
canvas.create_image(40,40,image=image_1,anchor=NW)
canvas.create_image(415,40,image=image_2,anchor=NW)
canvas.create_image(40,415,image=image_3,anchor=NW)
canvas.create_image(415,415,image=image_4,anchor=NW)

canvas.pack(fill=BOTH)

win.mainloop()