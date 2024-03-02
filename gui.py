from emailServices import EmailService

class Gui:
    def __init__(self):
        self.email_service = EmailService()
        self.login()

    def login(self):
        print("This is your email service. Please log in. \n")
        self.sender = input("Enter your email: ")
        self.pwd = input("Enter your password: ")
        self.gui()
    
    def get_login_credentials(self, file_path):
        with open(file_path, "r") as file:
            self.sender = file.readline()
            self.pwd = file.readline()
            
    def gui(self):
        print("This is your email service. What do you want to do? \n")
        print("1. Send an email \n")
        print("2. Read your latest 5 emails \n")
        print("3. Exit \n")
        choice = input("Enter your choice: ")
        match choice:
            case "1":
                receiver = input("Enter the reciever email: ")
                subject = input("Enter the subject: ")
                body = input("Enter the body: ")
                self.email_service.send_email(subject, body, self.sender, receiver, self.pwd)
            case "2":
                self.email_service.read_mail(receiver, self.pwd)
            case "3":
                exit()
            case _:
                print("Invalid choice. Please try again.")
                self.gui()