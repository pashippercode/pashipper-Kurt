from tkinter import *
from tkinter.messagebox import showinfo
from random import randint
f=open('18班人员名单.txt')
line = f.read().strip() #读取第一行
a=line.split('\n')
f.close() # 关闭文件
root = Tk('随机点名器','random','随机点名器')                   # 创建窗口对象的背景色
root.geometry('250x220')
li     = ['点击“OK”以随机点名']
listb  = Listbox(root)          #  创建两个列表组件
b=[]
#help(listb)
for item in li:                 # 第一个小部件插入数据
    listb.insert(0,item)
def helloCallBack():
    k=a[randint(0,len(a)-1)]
    while k in b:k=a[randint(0,len(a)-1)]
    b.append(k)
    showinfo( "随机点名：",k )
    #print(listb.__dict__)
    if len(b)>1:
        listb.delete(0,1)
    listb.insert(0,f'{k}')
    listb.insert(0,'抽取历史:')
    listb.insert(0,f'已抽取人数:{len(b)}')
    listb.pack
B =Button(root, text ="OK", command = helloCallBack)
listb.pack()# 将小部件放置到主窗口中
B.pack()
root.mainloop()                 # 进入消息循环

