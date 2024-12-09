from tkinter import *

win = Tk()

scrollbar_x = Scrollbar(win,orient=HORIZONTAL)
scrollbar_x.pack(side=BOTTOM,fill=X)

scrollbar_y = Scrollbar(win)
scrollbar_y.pack(side=RIGHT,fill=Y)

mylist = Listbox(win,xscrollcommand=scrollbar_x.set,yscrollcommand=scrollbar_y.set)

for i in range(60):
    mylist.insert(END, '此生唯爱雨妈和Mili,快说你永远喜欢Mili！！！' + str(i))
mylist.pack(side=LEFT,fill=BOTH)

scrollbar_x.config(command=mylist.xview)
scrollbar_y.config(command=mylist.yview)

win.mainloop()
