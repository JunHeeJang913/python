from tkinter import *
import tkinter.ttk as ttk


root = Tk()
root.title("NadoGUI")
root.geometry('640x480')

values = [str(i) + '일' for i in range(1,32)]
cmbx = ttk.Combobox(root, height= 5, values = values, state = "readonly")
cmbx.pack()
cmbx.set("카드 결제일")
cmbx.current(0)


def btncmd():
    print(cmbx.get())

btn = Button(root, text = 'choice', command=btncmd)
btn.pack()

root.mainloop()