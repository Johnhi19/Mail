from tkinter import *

class Gui:
    def __init__(self):
        self.master = Tk()
        self.master.geometry('500x500')

        self.login_frame = Frame(self.master)
        self.error_frame = Frame(self.master)
        self.nogmail_error_frame = Frame(self.master)
        self.welcome_frame = Frame(self.master)


    def login_screen(self):
        Label(self.login_frame, text='E-Mail').grid(row=0)
        Label(self.login_frame, text='Password').grid(row=1)

        self.e1 = Entry(self.login_frame, width=50)
        self.e1.grid(row=0, column=1)
        self.e2 = Entry(self.login_frame, width=50)
        self.e2.grid(row=1, column=1)

        Button(self.login_frame, text='Login', command=self.save_input).grid(row=3, column=1, columnspan=2, pady=4)
        self.login_frame.pack()

    def error_screen_nogmail(self):
        Label(self.nogmail_error_frame, text='Please enter a valid gmail address').pack()
        Button(self.nogmail_error_frame, text='Try Again', command=self.login_screen).pack()
        self.nogmail_error_frame.pack()

    def save_input(self):
        self.email = self.e1.get()
        self.pwd = self.e2.get()
        self.check_input()
    
    def check_input(self):
        if not self.email.endswith('@gmail.com'):
            self.login_frame.pack_forget()
            self.error_screen_nogmail()
        else:
            self.login_frame.pack_forget()
            self.welcome_frame.pack()

    def run(self):
        self.login_screen()
        self.master.mainloop()


gui = Gui()
gui.run()