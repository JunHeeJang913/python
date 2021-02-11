from tkinter import *

root = Tk()
root.title("NadoGUI")
root.geometry('640x480')

listbox = Listbox(root, selectmode='extended', height = 0)
listbox.insert(0, 'apple')
listbox.insert(1, 'strawberry')
listbox.insert(END, 'watermelon')
listbox.pack()

def btncmd():
    pass

btn = Button(root, text = 'click', command=btncmd)
btn.pack()

root.mainloop()