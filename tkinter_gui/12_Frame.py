import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("NadoGUI")
root.geometry('640x480')

Label(root, text="take a menu").pack(side='top')

Button(root, text="order").pack(side='bottom')

frameBurger = Frame(root, relief='solid', bd = 1)
frameBurger.pack(side = 'left', fill='both', expand=True)
Button(frameBurger, text = "ham").pack()
Button(frameBurger, text = "cheese").pack()
Button(frameBurger, text = "chicken").pack()

frameDrink = LabelFrame(root, relief = 'solid', text = "Drink")
frameDrink.pack(side = 'right', fill='both', expand=True)
Button(frameDrink, text = "Coke").pack()
Button(frameDrink, text = "Cide").pack()

root.mainloop()