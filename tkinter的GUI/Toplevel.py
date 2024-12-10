import tkinter as tk

root = tk.Tk()
root.iconbitmap("猫猫.ico")
root.title("顶级窗口")
root.geometry("500x300")
def create():
    toplevel = tk.Toplevel()
    toplevel.title("该干饭了")
    toplevel.geometry("150x100")
    msg = tk.Message(toplevel,text="今天中午吃什么？")
    msg.pack()

button = tk.Button(root,text="点我创建窗口！",command=create)
button.pack(side=tk.TOP)

root.mainloop()