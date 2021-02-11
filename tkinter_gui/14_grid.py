from tkinter import *
import tkinter.ttk as ttk
import time
#TODO: grid, button의 padx, pady글자, 이미지 기준 여백(grid에도 가능)
#width, height
root = Tk()
root.title("NadoGUI")
root.geometry('640x480')

btn = Button(root, text = "btn1", padx = 10, pady= 10)

btn.grid(row=0,column=0, rowspan=3, columnspan=5, sticky=N+E+W+S)


root.mainloop()