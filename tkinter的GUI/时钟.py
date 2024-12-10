import time
import tkinter as tk
class Clock(tk.Tk):
    def  __init__(self) -> None:
        super().__init__()
        x = int((self.winfo_screenwidth() - self.winfo_reqwidth() ) / 3)
        y = int((self.winfo_screenheight() - self.winfo_reqheight()) / 2.5)
        self.title("桌面时钟")
        self.time_text = ""
        self.label = tk.Label(self,text=self.time_text,
                                            bg="black",fg="cyan",
                                            font=("ds-digital",80),padx=10,pady=10)
        self.label.pack()
        self.geometry(f"600x230+{x}+{y}")
        self.update_time()
    def update_time(self):
        self.time_text = time.strftime("%y-%m-%d\n%H:%M:%S %p")
        self.label.config(text=self.time_text)
        self.after(1000,self.update_time)
if __name__ == '__main__':
    app = Clock()
    app.mainloop()