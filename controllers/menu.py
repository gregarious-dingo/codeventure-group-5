from controllers.login_system import LoginSystem
from resources.learning_modules import Learning_Modules
from users.learner import Learner
from users.parent import Parent
from users.educator import Educator
from utils.utils import Utils


class Menu:
    def __init__(self):
        self.login_system = LoginSystem()
        self.learning_modules = Learning_Modules()
    
    def login_menu(self):
        while True:
            self.login_system.print_menu()

            while True:
                try:
                    user_input = int(input("Please select a menu option: "))
                    break  # Break the loop if the input is a valid integer
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")
                    
            if user_input == 1:
                login_account = self.login_system.user_login()
                if not login_account:
                    continue
                elif login_account.account_type == "Learner":
                    Utils.display_str("Successfully logged in as a Learner!")
                    self.learner_menu(login_account)
                elif login_account.account_type == "Parent":
                    Utils.display_str("Successfully logged in as a Parent!")
                    self.parent_menu(login_account)
                elif login_account.account_type == "Educator":
                    Utils.display_str("Successfully logged in as an Educator!")
                    self.educator_menu(login_account)
            elif user_input == 2:
                self.login_system.user_register()
            elif user_input == 3:
                self.login_system.turn_off()
                break
            else:
                Utils.invalid_input()

    def learner_menu(self, account):
        while True:
            if account.blocked:
                Utils.display_str("Account Blocked")
                print("It appears someone has been spending too much time on their computer..")
                return

            print("You have the following options:")
            print("\t1. Select a learning module")
            print("\t2. Check your progress")
            print("\t3. Log out")

            while True:
                try:
                    user_input = int(input("Please select a menu option: "))
                    break  # Break the loop if the input is a valid integer
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")

            if user_input == 1:
                self.learning_modules.select_level(account)
            elif user_input == 2:
                account.progress_tracker.display_progress()
            elif user_input == 3:
                Utils.display_str("---- Logged out ----")
                break
            else:
                Utils.invalid_input()

    def parent_menu(self, account):
        while True:
            print("You have the following options:")
            print("\t1. Check your child's progress")
            print("\t2. Block child's account")
            print("\t3. Unblock child's account")
            print("\t4. Log out")

            while True:
                try:
                    user_input = int(input("Please select a menu option: "))
                    break  # Break the loop if the input is a valid integer
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")

            if user_input == 1:
                Utils.display_str(f"{account.learner.username}'s progress:")
                account.learner.progress_tracker.display_progress()
            elif user_input == 2:
                account.block_learner()
                Utils.display_str(f"{account.learner.username}'s account is blocked!")
            elif user_input == 3:
                account.unblock_learner()
                Utils.display_str(f"{account.learner.username}'s account is unblocked!")
            elif user_input == 4:
                Utils.display_str("---- Logged out ----")
                break
            else:
                Utils.invalid_input()
    
    def educator_menu(self):
        while True:
            print("You have the following options:")
            print("\t1. Modify learning module")
            print("\t2. Check learner progress")
            print("\t3. Log out")

            while True:
                try:
                    user_input = int(input("Please select a menu option: "))
                    break  # Break the loop if the input is a valid integer
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")

            if user_input == 1:
                print("Work in progress")
            elif user_input == 2:
                Utils.display_str(f"{account.learner.username}'s progress:")
                account.learner.progress_tracker.display_progress()
            elif user_input == 3:
                Utils.display_str("---- Logged out ----")
                break
            else:
                Utils.invalid_input()
