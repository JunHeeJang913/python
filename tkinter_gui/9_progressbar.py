from tkinter import *
import tkinter.ttk as ttk
import time

root = Tk()
root.title("NadoGUI")
root.geometry('640x480')

#progressbar = ttk.Progressbar(root, max = 100, mode = 'indeterminate')
#progressbar.start(10) # 10ms
#progressbar.pack()
#
#progressbar2 = ttk.Progressbar(root, max = 100, mode = 'determinate')    #달이 차오른다~~
#progressbar2.start(10) # 10ms
#progressbar2.pack()


#def btncmd():
#    progressbar2.stop()
#
#btn = Button(root, text = 'stop', command=btncmd)
#btn.pack()

var = DoubleVar()
pgbar = ttk.Progressbar(root, maximum=100, length=150, variable=var)
pgbar.pack()

def btncmd():
    for i in range(101):
        time.sleep(0.01) #0.01초 대기
        var.set(i)
        pgbar.update()


btn = Button(root, text = 'start', command=btncmd)
btn.pack()

root.mainloop()