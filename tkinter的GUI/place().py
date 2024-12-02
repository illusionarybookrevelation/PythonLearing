from tkinter import *
win = Tk()

frame = Frame(win,relief=RAISED,borderwidth=2,width=400,height=300)
frame.pack(side=TOP,fill=BOTH,ipadx=5,ipady=5,expand=1)

button_1 = Button(frame,text="若念",borderwidth=10)
button_1.place(x=40,y=40,anchor=W,width=80,height=40)

button_2 = Button(frame,text="无笙",borderwidth=10,command=frame.quit)
button_2.place(x=140,y=80,anchor=W,width=140,height=80)
win.mainloop()