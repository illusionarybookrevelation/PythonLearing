from tkinter import *

sports = ["棒球","篮球","足球","排球","网球"]

win = Tk()
label = Label(win)
label.pack()
def showSelection():
    choice = "你的选择是：" + sports[var.get()]
    label.config(text = choice)
var = IntVar()

Radiobutton(win,text=sports[0],variable=var,value=0,command=showSelection).pack(anchor=W)
Radiobutton(win,text=sports[1],variable=var,value=1,command=showSelection).pack(anchor=W)
Radiobutton(win,text=sports[2],variable=var,value=2,command=showSelection).pack(anchor=W)
Radiobutton(win,text=sports[3],variable=var,value=3,command=showSelection).pack(anchor=W)
Radiobutton(win,text=sports[4],variable=var,value=4,command=showSelection).pack(anchor=W)

win.mainloop()