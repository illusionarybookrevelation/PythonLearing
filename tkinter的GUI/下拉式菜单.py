from tkinter import *
import tkinter.messagebox

win = Tk()
win.title("下拉式菜单")

menu = Menu(win)
def doFileNewCommand(*args):
    tkinter.messagebox.askokcancel("菜单","您正在选择‘新建’菜单命令")

def doOpenFileCommand(*args):
    tkinter.messagebox.askokcancel("菜单","您正在选择‘打开’菜单命令")

def doFileSaveCommand(*args):
    tkinter.messagebox.askokcancel("菜单","您正在选择‘保存’菜单命令")
def doHelpContentsCommand(*args):
    tkinter.messagebox.askokcancel("菜单","您正在选择'文档'菜单命令")

def doHelpCoAboutCommand(*args):
    tkinter.messagebox.askokcancel("菜单","您正在选择'关于'菜单命令")

filename = Menu(menu, tearoff=0)
helpmenu = Menu(menu,tearoff=0)

filename.add_command(label="新建", command=doFileNewCommand)
filename.add_command(label="打开", command=doOpenFileCommand, accelerator="Ctrl-O")
filename.add_command(label="保存", command=doFileSaveCommand, accelerator="Ctrl-S")
filename.add_separator()
filename.add_command(label="退出", command=win.quit)

helpmenu.add_command(label="文档",command=doHelpContentsCommand,accelerator="F1")
helpmenu.add_separator()
helpmenu.add_command(label="关于",command=doHelpCoAboutCommand,accelerator="F2")

menu.add_cascade(label="文件", menu=filename)
menu.add_cascade(label="帮助",menu=helpmenu)

win.config(menu=menu)

win.bind("<Control-o>",doOpenFileCommand)
win.bind("<Control-O>",doOpenFileCommand)
win.bind("<Control-s>",doFileSaveCommand)
win.bind("<Control-S>",doFileSaveCommand)
win.bind("<F1>",doHelpContentsCommand)
win.bind("<F2>",doHelpCoAboutCommand)

win.mainloop()
