from tkinter import *
from tkinter import colorchooser,messagebox

win = Tk()
win.title("打开取色器")

def open_logcolor():
    color = my_color.show()
    messagebox.showinfo("提示","你选择的颜色为:" + color[1] + "\n" + \
                       "R = " + str(color[0][0]) + " G = " + str(color[0][1]) + " B = " + str(color[0][2]) )

my_color = colorchooser.Chooser(win)

Button(win,text="打开颜色对话框",command=open_logcolor).pack(side=LEFT)

win.mainloop()
