import tkinter as tk

def on_click(event):
    print(f"Clicked at ({event.x}, {event.y})")

def on_key(event):
    print(f"Key pressed: {event.keysym}")

root = tk.Tk()
root.title("事件绑定示例")

label = tk.Label(root, text="点击我或按键！", width=30, height=5, bg="lightblue")
label.pack()

# 绑定鼠标左键单击事件
label.bind("<Button-1>", on_click)

# 绑定键盘事件
root.bind("<Key>", on_key)

root.mainloop()
