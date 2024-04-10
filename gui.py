from tkinter import *
from emailServices import EmailService

class Gui(Tk):
    def __init__(self, *args, **kwargs): 
        Tk.__init__(self, *args, **kwargs)
        self.email_service = EmailService()

        container = Frame(self) 
        container.pack(side = "top", fill = "both", expand = True) 
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        self.frames = {} 
        
        for F in (StartPage, NogmailErrorPage, ChoicePage, WrongPwdOrMailErrorPage, SendPage, ReadPage):
            frame = F(container, self)
            self.frames[F] = frame 
            frame.grid(row = 0, column = 0, sticky ="nsew")
            self.show_frame(StartPage)

    def save_input(self, e1, e2):
        self.email = e1.get()
        self.pwd = e2.get()
        self.verify_input()
    
    def verify_input(self):
        if not self.email.endswith('@gmail.com'):
            self.show_frame(NogmailErrorPage)
        elif not self.email_service.verify_email_pwd(self.email, self.pwd):
            self.show_frame(WrongPwdOrMailErrorPage)
        else:
            self.show_frame(ChoicePage)

    def show_frame(self, cont):
    	frame = self.frames[cont]; frame.tkraise()

class StartPage(Frame):
    def __init__(self, parent, controller): 
        Frame.__init__(self, parent)

        Label(self, text='E-Mail').grid(row=0)
        Label(self, text='Password').grid(row=1)

        self.e1 = Entry(self, width=50)
        self.e1.grid(row=0, column=1)
        self.e2 = Entry(self, width=50)
        self.e2.grid(row=1, column=1)

        Button(self, text='Login', command= lambda: controller.save_input(self.e1, self.e2)).grid(row=3, column=1, columnspan=2, pady=4)

class NogmailErrorPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        Label(self, text='Please enter a valid gmail address').pack()
        Button(self, text='Try Again', command= lambda: controller.show_frame(StartPage)).pack()

class WrongPwdOrMailErrorPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        Label(self, text='Wrong email or password').pack()
        Button(self, text='Try Again', command= lambda: controller.show_frame(StartPage)).pack()

class ChoicePage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        Label(self, text='Welcome to your email client!').pack()
        Button(self, text='Send Email', command= lambda: controller.show_frame(SendPage)).pack()
        Button(self, text='Read Email', command= lambda: controller.show_frame(ReadPage)).pack()

class SendPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        Label(self, text='Send an email').pack()
        Button(self, text='Back', command= lambda: controller.show_frame(ChoicePage)).pack()

class ReadPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        Label(self, text='Read your emails').pack()
        Button(self, text='Back', command= lambda: controller.show_frame(ChoicePage)).pack()

gui = Gui()
gui.mainloop()