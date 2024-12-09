from tkinter import *
import tkinter.messagebox

win = Tk()
win.title("主目录菜单")

def start():
    tkinter.messagebox.askokcancel("菜单","您正在打开菜单....")

menu = Menu(win)

menu.add_command(label="文件",command=start)
menu.add_command(label="编辑",command=start)
menu.add_command(label="视图",command=start)
menu.add_command(label="帮助",command=start)

win.config(menu=menu)

win.mainloop()