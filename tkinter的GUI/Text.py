import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image,ImageTk
import time
def insert_text():
    """插入示例文本"""
    text_widget.insert("1.0", "しかのこのこのここしたんたん\n")

def clear_text():
    """清空文本框内容"""
    text_widget.delete("1.0", "end")

def save_to_file():
    """保存内容到文件"""
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt"),
                                                        ("All files", "*.*")])
    if file_path:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(text_widget.get("1.0", "end-1c"))  # 使用 "end-1c" 去除末尾的换行符
        messagebox.showinfo("保存成功", f"内容已保存到 {file_path}")

def quit_file():
    if tk.messagebox.askokcancel("退出","小鹿会一直注视着你的...."):
        root.destroy()

# 创建主窗口
root = tk.Tk()
root.title("鹿乃子乃子虎视眈眈-OP")

# 创建Text控件
text_widget = tk.Text(root, wrap="word", width=60, height=20)
text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# 创建滚动条并关联Text控件
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text_widget.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=text_widget.yview)

# 创建按钮功能区
button_frame = tk.Frame(root)
button_frame.pack(side=tk.BOTTOM, fill=tk.X)

btn_insert = tk.Button(button_frame, text="插入文本", command=insert_text)
btn_insert.pack(side=tk.LEFT, padx=5, pady=5)

btn_clear = tk.Button(button_frame, text="清空内容", command=clear_text)
btn_clear.pack(side=tk.LEFT, padx=5, pady=5)

btn_save = tk.Button(button_frame, text="保存到文件", command=save_to_file)
btn_save.pack(side=tk.LEFT, padx=5, pady=5)

root.protocol("WM_DELETE_WINDOW",quit_file)

img = Image.open("虎视眈眈.gif")
frames = []
try:
    while True:
        frames.append(ImageTk.PhotoImage(img))
        img.seek(len(frames))
except EOFError:
    pass

label = tk.Label(root)
label.pack(side=tk.TOP,fill=tk.X)

while True:
    for img_s in frames:
        label.config(image=img_s)
        root.update()
        time.sleep(0.1)


