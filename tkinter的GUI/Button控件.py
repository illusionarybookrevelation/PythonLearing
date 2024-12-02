from tkinter import *
import tkinter.messagebox

def on_link():
    button.flash()
    print("按键被点击了")

def cancel():
    if tkinter.messagebox.askokcancel("提示","要关闭此窗口吗？"):
        win.destroy()

win = Tk()
win.title("按键控件")

button = Button(win,text="点我啊！",relief=GROOVE,borderwidth=10,command=on_link,fg="#FF3333",bg="#99FFFF")
button.pack(pady=20)

win.protocol("WM_DELETE_WINDOW",cancel)

win.mainloop()

