from tkinter import *

win = Tk()
win.title(string = "古诗鉴赏")
Label(win,background="#00ff00",text="两个黄鹂鸣翠柳，一行白鹭上青天。").pack()
Label(win,background="SystemHighlight",text="窗含西岭千秋雪，门泊东吴万里船。").pack()
Button(win,padx=20,pady=20,text="关闭",command=win.quit).pack()
win.mainloop()