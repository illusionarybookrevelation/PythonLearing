from tkinter import *

win = Tk()
#文字与边框之间水平距离为20像素。
Button(win,padx=20,text="关闭",command=win.quit).pack()
#还可以使用其他测量单位,如cm(厘米),mm(毫米),i(英寸),p(点，1p=1/72英寸)。
Button(win,padx="2c",text="关闭",command=win.quit).pack()
Button(win,padx="8m",text="关闭",command=win.quit).pack()
Button(win,padx="2i",text="关闭",command=win.quit).pack()
Button(win,padx="20p",text="关闭",command=win.quit).pack()
win.mainloop()

