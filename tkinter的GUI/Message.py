from tkinter import *

root = Tk()
root.title("美丽的神话")

tsg = ("万世沧桑唯有爱是永远的神话，潮起潮落始终不悔真爱的相拥  \
        几番苦痛的纠缠多少黑夜挣扎，紧握双手让我和你再也不离分")

msg = Message(root,text=tsg,width=400)

msg.pack()

root.mainloop()