from tkinter import *

root = Tk()

root.geometry('300x400')

mybutton = Button(root, text='Hell World', font=('Helvetica', 14))
mybutton.place(relx=.5, rely=.5, anchor=CENTER)

root.mainloop()