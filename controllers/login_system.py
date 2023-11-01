from users.user import User
from users.learner import Learner
from users.parent import Parent
from users.educator import Educator
from utils.utils import Utils
import codecs

class LoginSystem:
    def __init__(self):
        self.file_path = "./data/users.txt"
        self.load_users()

    def load_users(self): 
        """
        Load list of users from the ./data/users.txt file
        :return: bool (True if successful, False otherwise)
        Inspired by FIT1056.
        """
        try:
            with open(self.file_path, "r", encoding="utf8") as users_f:
                self.users: [User] = []
                users_lines = users_f.readlines()
                for line in users_lines:
                    (username, password, account_type, learner) = line.strip().split(";")
                    account = None

                    password = codecs.decode(password, 'rot13')
                    if account_type == "Learner":
                        account = Learner(username, password)
                    elif account_type == "Parent":
                        for user in self.users:
                            if user.username == learner:
                                account = Parent(username, password, user)
                    else:
                        account = Educator(username, password)
                    self.users.append(account)
            return True
        except FileNotFoundError:
            print(f"The file \"{self.file_path}\" does not exist!")
            return False

    def print_menu(self):
        print("You have the following options:")
        print("\t1. Login")
        print("\t2. Register")
        print("\t3. Turn Off")
        
    def user_login(self):
        username = input("Enter your username: ")
        if self.username_available(username):
            Utils.display_str("User is not registered!")
            return
        password = input("Enter your password: ")

        authenticated = self.authenticate_user_login(username, password)
        if authenticated:
            return authenticated
        else:
            Utils.display_str("Wrong password!")
            return

    # def user_register(self):
    #     username = input("Enter your new username: ")
    #     while self.username_available(username) == False:
    #         Utils.display_str(f'Username {username} already taken!')
    #         username = input("Enter your new username: ")
    #     password = input("Enter your new password: ")

    #     print("----------------------")
    #     print("1. Learner\n2. Parent")
    #     print("----------------------")
    #     account_type_input = input("Enter the type of account to be registered: ")
    #     child = None

    #     if account_type_input == '1':
    #         account_type_input = "Learner"
    #         account = Learner(username, password)
    #         self.users.append(account)
    #         Utils.display_str("Account successfully registered!")

    #     elif account_type_input == '2':
    #         account_type_input = "Parent"
    #         # Ask for parent's learner
    #         child = input("Please enter the username of your child: ")
    #         while self.find_account_type(child) != "Learner" or self.username_available(child):
    #             Utils.display_str("That Learner does not exist!")
    #             child = input("Please enter the username of your child: ")   

    #         child = self.return_user(child)
    #         account = Parent(username, password, child)
    #         self.users.append(account)

    #         Utils.display_str("Account successfully registered!")
    #     #elif account_type_input == '3':
    #         #print("Work in progress")

    #     else:
    #         Utils.invalid_input()
    #         return

    #     try:
    #         with open("./data/users.txt", "a") as database:
    #             # Write data to the next empty line in the file
    #             if account_type_input == "Learner":
    #                 database.write(f"{username};{password};Learner;NA\n")  # '\n' to add a newline
    #             elif account_type_input == "Parent":
    #                 database.write(f"{username};{password};Parent;{child.username}\n")
    #     except FileNotFoundError:
    #         print("The file or directory does not exist.")

    def user_register(self, username, password, user_type, *child):
        try:
            with open("./data/users.txt", "a") as database:
                if user_type == "Parent":
                    new_account = Parent(username, password, child)
                    self.users.append(new_account)

                    encrypted = codecs.encode(password, 'rot13')
                    database.write(f"{username};{encrypted};{user_type};{child[0]}\n")
                elif user_type == "Educator":
                    new_account = Educator(username, password)
                    self.users.append(new_account)

                    encrypted = codecs.encode(password, 'rot13')
                    database.write(f"{username};{encrypted};{user_type};NA\n")
                elif user_type == "Learner":
                    new_account = Learner(username, password)
                    self.users.append(new_account)

                    encrypted = codecs.encode(password, 'rot13')
                    database.write(f"{username};{encrypted};{user_type};NA\n")
                
        except FileNotFoundError:
            print("The file or directory does not exist.")

    def validate_username_register(self, username):
        if not username:
            return False
        else:            
            return True

    def validate_password_register(self, password):
        if not password:
            print("Password has been ")
            return False
        elif len(password) < 8:
            return False
        elif not any(char.isdigit() for char in password):
            return False
        elif not any(char.isupper() for char in password):
            return False
        elif not any(char.islower() for char in password):
            return False
        else:
            return True
        
    def validate_user_type_register(self, user_type):
        if not user_type:
            return False
        else:            
            return True

    def turn_off(self):
        Utils.display_str("You have turned off the machine.")

    def username_available(self, username):
        for user in self.users:
            if user.username == username:
                return False
        return True

    def find_account_type(self, username):
        for user in self.users:
            if user.username == username:
                return user.account_type

    def authenticate_user_login(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                return user
        return False

    def return_user(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return False
        
