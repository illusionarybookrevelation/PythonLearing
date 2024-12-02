import tkinter as tk

def on_key_press(event):
    """处理按键按下的事件"""
    # 将输入改为暗文显示，按键符号替换为 "*"
    label.config(text=f"输入你的密码，暗文输入：{'*' * len(event.keysym)}")

def focus_on_button(event):
    """点击按钮时让其获取焦点"""
    button.focus_set()

# 创建主窗口
root = tk.Tk()
root.title("按键绑定示例")

# 创建标签
label = tk.Label(root, text="Click the button and press a key", font=("Arial", 16))
label.pack(pady=20)

# 创建按钮
button = tk.Button(root, text="Focus me", font=("Arial", 14))
button.pack(pady=20)

# 绑定按键事件到按钮
button.bind("<Key>", on_key_press)

# 点击按钮时让其获取焦点
button.bind("<Button-1>", focus_on_button)

root.mainloop()
