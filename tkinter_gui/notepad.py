from tkinter import *
import os

root = Tk()
root.title('제목없음 - Windows 메모장')
root.geometry('640x480')

fileName = "Mynote.txt"

#메뉴
menu = Menu(root)

def fopen():
    if os.path.isfile(fileName):
        with open(fileName, 'r', encoding = 'utf8') as file:
            txt.delete('1.0', END)
            txt.insert(END, file.read())


def save():
    with open(fileName, 'w', encoding='utf8') as file:
        file.write(txt.get('1.0', END))

menuFile = Menu(menu, tearoff=0)
menuFile.add_command(label="Open", command = fopen)
menuFile.add_command(label="Save",command = save)
menuFile.add_separator()
menuFile.add_command(label="Exit", command = root.quit)
menu.add_cascade(label = 'File', menu = menuFile)

menuEdit = Menu(menu, tearoff=0)
menu.add_cascade(label = 'Edit', menu = menuEdit)
menuTemplate = Menu(menu, tearoff=0)
menu.add_cascade(label = 'Template', menu = menuTemplate)
menuView = Menu(menu, tearoff=0)
menu.add_cascade(label = 'View', menu = menuView)
menuHelp= Menu(menu, tearoff=0)
menu.add_cascade(label = 'Help', menu = menuHelp)

menu.config(menu=menu)

#스크롤바
scrlbar =Scrollbar(root)
scrlbar.pack(side="right", fill ="y")

#본문
txt = Text(root, yscrollcommand=scrlbar.set)
txt.pack(side = 'left', fill='both', expand=True)
scrlbar.config(command=txt.yview)

root.mainloop()