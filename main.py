from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("我的第一个GUI")
root.geometry("500x300+100+200")#tkinter．主窗口
# 主窗口位置和大小
# 通过geometry('wxh±x±y，）进行设置·w为宽度，h为高度·
# +X表示距屏幕左边的距离；-x表示距屏幕右边的距离，
# +Y表示距屏幕上边的距离；-y表示距屏幕下边的距离·

btn01=Button(root)#建立一个button对象，放到窗口里来
btn01["text"]="点我送花"
btn01.pack()#布局管理器，将button合理的放到窗口中


def songhua(e):#e事件对象
    messagebox.showinfo("Message","送你一朵玫瑰花，亲亲我吧")
    print("送你99朵玫瑰花")

btn01.bind("<Button-1>",songhua)#songhua函数与鼠标左键绑定，
root.mainloop() #只有加这一句窗口才能出现，进入 事件循环，监听用户，这是个独立的线程