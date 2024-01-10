import random
from tkinter import *
list=['蜜雪冰城','华莱士','烤鱼','烧烤','阳阳中国饭','烤肉']
#显示随时菜单中的一个菜名
def muil():
    print(random.choice(list))
#插入一个菜单选项
def insert():
    list1=str(input('请输入一个菜单名称'))
    list.append(list1)
    print(list)
#查询新菜单
def newmuil():
    print(list)
#删除一个菜单选项
def delmuil():
    print(list)
#    str=int(input('输入数字'))
    tiaojian=True
    while tiaojian:
        str=int(input('输入数字'))
        if str>len(list):
            print('超出菜单范围，请从新输入')
            continue
        else:
            del list[str]
            print(list)
            break
print(list)
tk=Tk()
butt1=Button(tk,text='随机产生一个菜单',comman=muil)
butt2=Button(tk,text='插入一个新的菜单',comman=insert)
butt3=Button(tk,text='删除一个菜单内容',comman=delmuil)
butt4=Button(tk,text='新的菜单',comman=newmuil)
#butt5=Button(tk,text='',comman=muil)
butt1.pack()
butt2.pack()
butt3.pack()
butt4.pack()
#butt5.pack()
