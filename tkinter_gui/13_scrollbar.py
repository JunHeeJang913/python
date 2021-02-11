from tkinter import *
import tkinter.ttk as ttk
import time

root = Tk()
root.title("NadoGUI")
root.geometry('640x480')

frame = Frame(root)
frame.pack()

scrlbar = Scrollbar(frame)
scrlbar.pack(side='right', fill='y')

listbox = Listbox(frame, selectmode='extended', height= 10, yscrollcommand=scrlbar.set)
for i in range(1,32):
    listbox.insert(END,str(i)+'일')
listbox.pack(side='left')


scrlbar.config(command=listbox.yview)

root.mainloop()