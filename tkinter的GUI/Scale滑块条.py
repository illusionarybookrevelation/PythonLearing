from tkinter import *
win = Tk()

def getRGBStr(value):
    ret = str(hex(int(value/130*255)))
    ret = ret[2:4]
    ret = str.zfill(ret,2)
    return ret

def showRGBColor():
    str_R = getRGBStr(var1.get())
    str_G = getRGBStr(var2.get())
    str_B = getRGBStr(var3.get())
    color = "#" + str_R + str_G + str_B
    colorBar.config(background=color)

var1 = DoubleVar()
var2 = DoubleVar()
var3 = DoubleVar()

colorBar = Label(win,text=" " * 40,background="#000000")
colorBar.pack(side=TOP)

scale1 = Scale(win,variable=var1)
scale2 = Scale(win,variable=var2)
scale3 = Scale(win,variable=var3)

scale1.pack(side=LEFT)
scale2.pack(side=LEFT)
scale3.pack(side=LEFT)

button = Button(win,text="查看",command=showRGBColor)
button.pack(side=BOTTOM)

win.mainloop()