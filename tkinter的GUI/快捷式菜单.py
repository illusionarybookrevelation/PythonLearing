from tkinter import *
import tkinter.messagebox

win = Tk()
win.title("快捷式菜单")

popupmenu = Menu(win,tearoff=0)

def doSomething():
    tkinter.messagebox.askokcancel("菜单","你正在选择快捷式菜单命令")

popupmenu.add_command(label="复制",command=doSomething)
popupmenu.add_command(label="粘贴",command=doSomething)
popupmenu.add_command(label="剪切",command=doSomething)
popupmenu.add_command(label="删除",command=doSomething)

def showPopuUPMenu(event):
    popupmenu.post(event.x_root,event.y_root)

win.bind("<Button-3>",showPopuUPMenu)

win.mainloop()