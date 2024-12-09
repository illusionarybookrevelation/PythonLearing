import tkinter.messagebox
from tkinter import *

win = Tk()
win.title("calc")

frame = Frame(win)

def calc():
    result = "= " + str(eval(expression.get()))
    lable.config(text=result)

def clear():
    expression.set("")
    lable.config(text="")

def cancel():
    if tkinter.messagebox.askokcancel("提示","要关闭计算器吗?"):
        win.destroy()

lable = Label(frame)
expression = StringVar()
entry = Entry(frame,textvariable=expression)
entry.pack()

button1 = Button(frame,text="等于",command=calc)
button2 = Button(frame,text="清除",command=clear)

entry.focus()
frame.pack()

lable.pack(side=LEFT)
button1.pack(side=RIGHT)
button2.pack(side=RIGHT)

win.protocol("WM_DELETE_WINDOW",cancel)

frame.mainloop()
