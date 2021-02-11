from tkinter import *

root = Tk()
root.title("NadoGUI")
root.geometry('640x480')

chkvar = IntVar()
chkbox = Checkbutton(root, text = "오늘 하루 보지 않기", variable=chkvar)
#chkbox.select() # 자동 선택
#chkbox.deselect() #선택 해제 
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text = '일주일동안보지않기', variable=chkvar2)
chkbox2.pack()

def btncmd():
    print(chkvar.get())     #0: 체크 안됨, 1:체크 됨
    print(f': {chkvar2.get()}')

btn = Button(root, text = 'click', command=btncmd)
btn.pack()

root.mainloop()