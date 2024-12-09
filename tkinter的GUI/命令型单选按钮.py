from tkinter import *

sports = ["棒球","篮球","足球","排球","网球"]

win = Tk()
label = Label(win)
label.pack()
def showSelection():
    choice = "你的选择是：" + sports[var.get()]
    label.config(text = choice)
var = IntVar()

radio0 = Radiobutton(win,text=sports[0],variable=var,value=0,command=showSelection)
radio1 = Radiobutton(win,text=sports[1],variable=var,value=1,command=showSelection)
radio2 = Radiobutton(win,text=sports[2],variable=var,value=2,command=showSelection)
radio3 = Radiobutton(win,text=sports[3],variable=var,value=3,command=showSelection)
radio4 = Radiobutton(win,text=sports[4],variable=var,value=4,command=showSelection)

radio0.config(indicatoron=False)
radio1.config(indicatoron=False)
radio2.config(indicatoron=False)
radio3.config(indicatoron=False)
radio4.config(indicatoron=False)

radio0.pack(anchor=W)
radio1.pack(anchor=W)
radio2.pack(anchor=W)
radio3.pack(anchor=W)
radio4.pack(anchor=W)

win.mainloop()