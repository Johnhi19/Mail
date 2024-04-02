from tkinter import *

def save_input():
    email = e1.get()
    pwd = e2.get()
    print(f"Email: {email}, Password: {pwd}")

master = Tk()
Label(master, text='E-Mail').grid(row=0)
Label(master, text='Password').grid(row=1)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(master, text='Quit', command=save_input).grid(row=3, column=0, sticky=W, pady=4)

mainloop()