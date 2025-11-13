import tkinter as tk
from PIL import Image, ImageTk
import tkinter.messagebox
import pygame
class Mother(tk.Tk):
    def __init__(self):
        super().__init__()
        self.frames = []
        self.image = ""
        self.title("Window 11 System Doodle Dance")
        self.iconbitmap('./ico/仙.ico')
        x = int((self.winfo_screenwidth() - self.winfo_reqwidth()) / 5)
        y = int((self.winfo_screenheight() - self.winfo_reqheight()) / 5)
        self.label = tk.Label(self, image=self.image,bg="black")
        self.label.pack()
        self.geometry(f"960x540+{x}+{y}")
        self.protocol("WM_DELETE_WINDOW",self.quit)
        self.gif_image()
        # 解开封印
        self.pygame_playsound()
        self.update()
    def gif_image(self):
        self.image = Image.open('./gif/win11娘.gif')
        try:
            while True:
                frame = ImageTk.PhotoImage(self.image)
                self.frames.append(frame)
                self.image.seek(self.image.tell() + 1)
        except EOFError:
            pass
    def update(self, idx=0):
        if idx < len(self.frames):
            self.label.config(image=self.frames[idx])
            idx += 1
            self.after(30, lambda: self.update(idx))
        else:
            idx = 0
            self.update(idx)
    @staticmethod
    def pygame_playsound():
        pygame.init()
        pygame.mixer.music.load("./player/doodle.mp3")
        pygame.mixer.music.play(-1)
    def quit(self):
        if tk.messagebox.askokcancel("退出","确定要退出？不留下来看会儿吗？"):
            self.destroy()
if __name__ == '__main__':
    app = Mother()
    app.mainloop()
