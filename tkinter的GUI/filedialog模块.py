from tkinter import *
import tkinter.filedialog

win = Tk()
win.title("打开文件与保存文件")
def create_open():
    may_log1.show()
def create_save():
    may_log2.show()

MyFileType = [('Python files','*.py;*.pyw'),('All files','*')]

may_log1 = tkinter.filedialog.Open(win,filetypes=MyFileType)
may_log2 = tkinter.filedialog.SaveAs(win,filetypes=MyFileType)

Button(win,text="打开文件",command=create_open).pack(side=LEFT)
Button(win,text="保存文件",command=create_save).pack(side=LEFT)

win.mainloop()