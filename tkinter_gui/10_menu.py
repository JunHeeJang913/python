from tkinter import *
import tkinter.ttk as ttk
import time

root = Tk()
root.title("NadoGUI")
root.geometry('640x480')

menu = Menu(root)

def create_nfile():
    print("cnf")

#file menu
menu_file = Menu(menu, tearoff= 0)
menu_file.add_command(label="New File", command = create_nfile)
menu_file.add_command(label="New Window")
menu_file.add_separator()
menu_file.add_command(label = "Open File...")
menu_file.add_separator()
menu_file.add_command(label="Save All", state = 'disable')
menu_file.add_command(label = 'Exit', command=root.quit)

menu.add_cascade(label = "File", menu = menu_file)

#Edit menu(빈값)
menu.add_command(label = 'Edit')

#menu에 radio button
menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label="Python")
menu_lang.add_radiobutton(label="JAVA")
menu_lang.add_radiobutton(label="C++")

menu.add_cascade(label="Language", menu= menu_lang)

#Check box
menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label = "Show Minimap")
menu.add_cascade(label = "View", menu = menu_view)

root.config(menu = menu)

root.mainloop()