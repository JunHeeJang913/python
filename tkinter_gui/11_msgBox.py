import tkinter
import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("NadoGUI")
root.geometry('640x480')

def info():
    msgbox.showinfo("알림", "정상 예매")
def warn():
    msgbox.showwarning("경고", "ㅋㅋ")
def err():
    msgbox.showerror("error", "ㅋㅋ")
def okCancle():
    msgbox.askokcancel("확인/취소", "해당좌석은 유아동반석입니다. 예매하시겠습니까?")
def retryCancle():
    response = msgbox.askretrycancel("재시도/취소", "일시적 오류 다시 시도하겠습니까?")
    print(response) #True False None....

Button(root, command= info, text="알림").pack()
Button(root, command=warn, text="경고").pack()
Button(root, command=err, text="err").pack()
Button(root, command=okCancle, text = "asdf").pack()
Button(root, command=retryCancle, text = "asdf").pack()

root.mainloop()