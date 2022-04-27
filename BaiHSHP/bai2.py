from tkinter import *
 
top = Tk()
top.geometry("topmost", True)
button = Button(top, text = "Xac Nhan", command = helloCallback).place(x=30, y=150)
name = Label(top, text = "Name").place(x=30, y=50)
password = Label(top, text = "Mat Khau").place(x=30, y=90)
e1 = Entry(top).place(x=80, y=50)
e2 = Entry(top).place(x=80, y=90)
def helloCallback():
    if (e1 == "Nguyen Duc Viet"):
        button.pack(Command=helloCallback)
top.mainloop()