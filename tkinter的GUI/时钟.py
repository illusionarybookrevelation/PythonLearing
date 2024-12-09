import time
import tkinter as tk
class Clock(tk.Tk):
    def  __init__(self) -> None:
        super().__init__()

        self.title("桌面时钟")
        self.time_text = ""
        self.label = tk.Label(self,text=self.time_text,
                                            bg="black",fg="cyan",
                                            font=("ds-digital",80),padx=10,pady=10)
        self.label.pack()
        self.update_time()
    def update_time(self):
        self.time_text = time.strftime("%y-%m-%d\n%H:%M:%S %p")
        self.label.config(text=self.time_text)
        self.after(1000,self.update_time)
if __name__ == '__main__':
    app = Clock()
    app.mainloop()