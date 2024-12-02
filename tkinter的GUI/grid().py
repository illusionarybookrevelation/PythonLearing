from tkinter import *

win = Tk()

frame = Frame(win,relief=RAISED,borderwidth=2)
frame.pack(side=TOP,fill=BOTH,ipadx=5,ipady=5,expand=1)

for i in range(5):
    for j in range(5):
        Button(frame,text="(" + str(i) + "," + str(j) + ")").grid(row=i,column=j)

win.mainloop()