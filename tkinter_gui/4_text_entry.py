from tkinter import *

root = Tk()
root.title("NadoGUI")
root.geometry('640x480')

txt = Text(root, width= 30, height = 5)
txt.pack()

txt.insert(END, "글자를 입력하세요")

e = Entry(root, width = 30)
e.pack()
e.insert(0, '한줄만 입력하세요')

def btncmd():
    print(txt.get('1.0', END))  # 1: 첫번째 라인, 0 : 0번째 column 위치     1.0 부터 끝까지
    print(e.get())

    txt.delete('1.0', END)
    e.delete(0,END)

    txt.insert(END, "글자를 입력하세요")
    e.insert(0, '한줄만 입력하세요')

btn = Button(root, text = 'click', command=btncmd)
btn.pack()

root.mainloop()