"""文档介绍：测试一个经典的GUI程序写法，使用面向对象模式"""
import tkinter as tk
from tkinter import messagebox


class Application(tk.Frame):
    """一个经典的GUI程序"""

    def __init__(self, master=None):
        # 定义构造函数
        super().__init__(master)  # 调用父类构造方法，传入master
        self.master = master
        self.pack()
        self.creatWidget()

    def creatWidget(self):
        """创建组件"""
        self.btn01 = tk.Button(self)  # 容器组件，传入master
        self.btn01["text"] = "点击送花"
        self.btn01.pack()
        self.btn01["command"] = self.songhua

        #创建推出按钮
        self.btnQuit=tk.Button(self,text="退出",command=self.destroy)#destroy是self自带的函数
        self.btnQuit.pack()

    def songhua(self):
        messagebox.showinfo("送花", "送你99朵玫瑰花")  # ("标题","文字提示")


root = tk.Tk()
root.geometry("400x200+200+200")
root.title("一个面向对象GUI测试")
app = Application(master=root)
root.mainloop()#这玩意必须写在app定义的下面，否则没有app
