from tkinter import *

win = Tk()

frame = Frame(win)

name = ["香蕉","苹果","橘子","荔枝","火龙果","甘蔗","椰子","山竹"]

listbox = Listbox(frame)
listbox.delete(0,END)
for i in range(8):
    listbox.insert(END,name[i])

listbox.pack()
frame.pack()
win.mainloop()