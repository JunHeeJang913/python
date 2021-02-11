from tkinter import *

root = Tk()
root.title("NadoGUI")

btn1 = Button(root, text = '버튼1')
btn1.pack() #이게 있어야 보임

btn2 = Button(root, padx= 5, pady= 10, text = '버튼2')  #여백
btn2.pack()

btn3 = Button(root, padx= 10, pady= 5, text = '버튼3')
btn3.pack()

btn4 = Button(root, width = 10, height= 3, text = 'btn4')   #고정크기
btn4.pack()

btn5 = Button(root, fg='red', bg='yellow', text = 'btn5')
btn5.pack()

photoImage = PhotoImage(file = "./img.png")
btn6 = Button(root, image = photoImage)
btn6.pack()

def btncmd():
    print("clicked")

btn7 = Button(root, text = 'working btn', command = btncmd)
btn7.pack()

root.mainloop()