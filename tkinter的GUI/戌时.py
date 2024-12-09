import tkinter as tk

dusk = tk.Tk()

x = int((dusk.winfo_screenwidth()  - dusk.winfo_reqwidth())/ 5.2)
y = int((dusk.winfo_screenheight() - dusk.winfo_reqheight()) / 10)

canvas = tk.Canvas(dusk,width=1024,height=711,highlightthickness=0)
img = tk.PhotoImage(file="./忍三/剑舞风华.png")
canvas.create_image(0,0,anchor=tk.NW,image=img)
canvas.pack()

dusk.title("忍者必须死3")
dusk.geometry(f"1024x711+{x}+{y}")
dusk.overrideredirect(True)

dusk.after(5000,lambda:dusk.destroy())
dusk.mainloop()