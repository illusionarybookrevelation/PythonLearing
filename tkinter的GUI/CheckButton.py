from tkinter import *

win = Tk()
check1 = Checkbutton(win,text="苹果")
check2 = Checkbutton(win,text="香蕉")
check3 = Checkbutton(win,text="梨子")
check1.select()
check1.pack(side=LEFT)
check2.pack(side=LEFT)
check3.pack(side=LEFT)
win.mainloop()