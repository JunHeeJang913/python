from tkinter import *

root = Tk()
root.title("NadoGUI")
root.geometry('640x480')

#택1
Label(root, text='메뉴를 선택하세요').pack()

menu = IntVar() #
btn_burger1 = Radiobutton(root, text='햄버거', value =1, variable= menu)
btn_burger2 = Radiobutton(root, text='치즈버거', value =2, variable= menu)
btn_burger3 = Radiobutton(root, text='치킨버거', value =3, variable= menu)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

Label(root, text = '음료를 선택하세요').pack()

drink = StringVar()
btn_drink1 = Radiobutton(root, text='콜라', value = 'coke', variable = drink)
btn_drink2 = Radiobutton(root, text='Cider', value = 'Cider', variable = drink)
btn_drink3 = Radiobutton(root, text='asdf', value = 'asdf', variable = drink)

btn_drink1.pack()
btn_drink2.pack()
btn_drink3.pack()


def btncmd():
    print(menu.get())
    print(drink.get())

btn = Button(root, text = '주문', command=btncmd)
btn.pack()

root.mainloop()