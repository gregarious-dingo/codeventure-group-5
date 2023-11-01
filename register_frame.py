import tkinter as tk
from controllers.login_system import LoginSystem

class RegisterFrame(tk.Frame):

    def __init__(self, master, login_frame):
        super().__init__(master)
        self.login_frame = login_frame

        register_title = tk.Label(self, text="Creat New Account",
                                  font=("Arial Bold", 25))
        register_title.grid(row=1, columnspan=2)

        reg_username_label = tk.Label(master=self, text="Enter your new username:")
        reg_username_label.grid(row=2, column=0)

        reg_password_label = tk.Label(master=self, text="Enter your new password:")
        reg_password_label.grid(row=3, column=0)

        self.reg_username_entry = tk.Entry(master=self, width=20)
        self.reg_username_entry.grid(row=2, column=1)

        self.reg_password_entry = tk.Entry(master=self, width=20, show="●")
        self.reg_password_entry.grid(row=3, column=1)

        type_user_label = tk.Label(master=self, text="What type of user are you registering as?")
        type_user_label.grid(row=4, column=0, sticky=tk.E)

        self.user_type = tk.StringVar()

        self.learner_button = tk.Radiobutton(self,
                                             text="Learner",
                                             variable=self.user_type,
                                             value="Learner",
                                             command=self.disable_parent_child)
        
        self.educator_button = tk.Radiobutton(self,
                                             text="Educator",
                                             variable=self.user_type,
                                             value="Educator",
                                             command=self.disable_parent_child)
        
        self.parent_button = tk.Radiobutton(self,
                                             text="Parent",
                                             variable=self.user_type,
                                             value="Parent",
                                             command=self.ask_for_parent_child)

        self.learner_button.grid(row=4, column=1, sticky=tk.W)
        self.educator_button.grid(row=5, column=1, sticky=tk.W)
        self.parent_button.grid(row=6, column=1, sticky=tk.W)

        register_button = tk.Button(self, text="Register", command=self.register)
        register_button.grid(row=8, columnspan=2, pady=50)

        self.register_text = tk.StringVar()
        register_message = tk.Label(self, textvariable=self.register_text)
        register_message.grid(row=9, columnspan=2)

        back_to_login_button = tk.Button(self, text="Back to Login", command=self.back_to_login)
        back_to_login_button.grid(row=10, columnspan=2)

    def ask_for_parent_child(self):
        self.child_label = tk.Label(self, text="Enter your child's username:")
        self.child_entry = tk.Entry(self)

        self.child_label.grid(row=7, column=0, sticky=tk.E)
        self.child_entry.grid(row=7, column=1, sticky=tk.W)

    def disable_parent_child(self):
        try:
            self.child_label.grid_remove()
            self.child_entry.grid_remove()
        except AttributeError:
            pass

    def register(self):
        username = self.reg_username_entry.get()
        password = self.reg_password_entry.get()
        user_type = self.user_type.get()

        if not username:
            self.register_text.set('Registration failed. Please enter a username.')
            return
        elif not password:
            self.register_text.set('Registration failed. Please enter a password.')
            return
        elif not self.login_frame.login_system.validate_username_register(username):
            self.register_text.set('Registration failed. Username must be at least 6 characters long and contain only letters and numbers.')
            return
        elif not self.login_frame.login_system.validate_password_register(password):
            self.register_text.set('Registration failed. Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, and one number.')
            return
        

        if self.login_frame.login_system.username_available(username):
            if self.login_frame.login_system.validate_user_type_register(user_type):

                if user_type == "Parent":
                    child_username = (self.child_entry.get())
                    if not child_username:
                        self.register_text.set("Registration failed. Please input your child's name.")
                        return
                    elif self.login_frame.login_system.find_account_type(child_username) != "Learner" or \
                        self.login_frame.login_system.username_available(child_username):
                        self.register_text.set(f"Registration failed. The learner {child_username} doesn't exist!")
                        return

                    self.login_frame.login_system.user_register(username, password, user_type, child_username)
                    self.register_text.set("Account successfully registered!")
                else:
                    self.login_frame.login_system.user_register(username, password, user_type)
                    self.register_text.set("Account successfully registered!")

            else:
                self.register_text.set('Registration failed. Please select a user type.')
                return
        else:
            self.register_text.set(f'Username "{username}" already taken.')

    def back_to_login(self):
        self.place_forget()
        self.login_frame.place(relx=0.5, rely=0.5, anchor= tk.CENTER)

        


