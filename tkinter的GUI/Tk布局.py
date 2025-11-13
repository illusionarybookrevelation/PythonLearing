from tkinter import *
from tkinter.ttk import *

class Win:
    def __init__(self):
        self.root=self._win()
        self.tk_label_1=self._tk_label_1()
        self.tk_input=self._tk_input()
        self.tk_label_2 = self._tk_label_2()
        self.tk_check_button_1 = self.__tk_check_button_1()
        self.tk_check_button_2 = self.__tk_check_button_2()
        self.tk_check_button_3 = self.__tk_check_button_3()
        self.tk_check_button_4 = self.__tk_check_button_4()
        self.tk_label_3 = self.__tk_label_3()
        self.tk_radio_button_1 = self.__tk_radio_button_1()
        self.tk_radio_button_2 = self.__tk_radio_button_2()
        self.tk_select_box = self.__tk_select_box()
        self.tk_label_4 = self.__tk_label_4()
        self.tk_button_1 = self.__tk_button_1()
        self.tk_button_2 = self.__tk_button_2()

    def _win(self):
        root = Tk()
        root.title("Tkinter布局")
        width = 600
        height = 500
        screenwidth= root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width,height,(screenwidth - width) / 2,(screenheight - height) / 2)
        root.geometry(geometry)
        root.resizable(width=False,height=False)
        return root
    def show(self):
        self.root.mainloop()
    def _tk_label_1(self):
        label=Label(self.root,text="姓名")
        label.place(x=50,y=60,height=24)
        return label
    def _tk_input(self):
        ipt=Entry(self.root)
        ipt.place(x=120,y=60,width=150,height=24)
        return ipt
    def _tk_label_2(self):
        label = Label(self.root, text="爱好")
        label.place(x=50, y=100, width=50, height=24)
        return label
    def __tk_check_button_1(self):
        cb = Checkbutton(self.root, text="唱")
        cb.place(x=120, y=100, width=54, height=24)
        return cb

    def __tk_check_button_2(self):
        cb = Checkbutton(self.root, text="跳")
        cb.place(x=190, y=100, width=54, height=24)
        return cb

    def __tk_check_button_3(self):
        cb = Checkbutton(self.root, text="rap")
        cb.place(x=260, y=100, width=54, height=24)
        return cb

    def __tk_check_button_4(self):
        cb = Checkbutton(self.root, text="篮球")
        cb.place(x=330, y=100, width=54, height=24)
        return cb

    def __tk_label_3(self):
        label = Label(self.root, text="性别")
        label.place(x=50, y=142, width=50, height=24)
        return label

    def __tk_radio_button_1(self):
        rb = Radiobutton(self.root, text="男")
        rb.place(x=120, y=140, width=57, height=24)
        return rb

    def __tk_radio_button_2(self):
        rb = Radiobutton(self.root, text="女")
        rb.place(x=190, y=140, width=57, height=24)
        return rb

    def __tk_select_box(self):
        cb = Combobox(self.root, state="readonly")
        cb['values'] = ("本科", "专科", "高中")
        cb.place(x=120, y=180, width=150, height=24)
        return cb

    def __tk_label_4(self):
        label = Label(self.root, text="学历")
        label.place(x=50, y=180, width=50, height=24)
        return label

    def __tk_button_1(self):
        btn = Button(self.root, text="登记")
        btn.place(x=100, y=410, width=143, height=40)
        return btn

    def __tk_button_2(self):
        btn = Button(self.root, text="清空")
        btn.place(x=340, y=410, width=143, height=40)
        return btn

if __name__ == '__main__':
    win = Win()
    win.show()
