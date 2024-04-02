from emailServices import EmailService

class Gui:
    def __init__(self):
        self.email_service = EmailService()
        self.login()

    def login(self):
        print("This is your email service. Please log in by either providing a path to the username and password (1.) or you can type in the user name and password manually (2.). \n")
        choice = input("Enter your choice: ")
        if choice == "1":
            path = input("Enter the path to your login credentials file: ")
            self.login_with_file(path)
        elif choice == "2":
            self.sender = input("Enter your email: ")
            self.pwd = input("Enter your password: ")
        else:
            print("Invalid choice. Please try again.")
            self.login()
        self.gui()

    def login_with_file(self, file_path):
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
                self.email_service.read_mail(self.sender, self.pwd)
            case "3":
                exit()
            case _:
                print("Invalid choice. Please try again.")
        self.gui()