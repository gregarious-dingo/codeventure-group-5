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

        reg_username_entry = tk.Entry(master=self, width=20)
        reg_username_entry.grid(row=2, column=1)

        reg_password_entry = tk.Entry(master=self, width=20)
        reg_password_entry.grid(row=3, column=1)

        type_user_label = tk.Label(master=self, text="What type of user are you registering as?")
        type_user_label.grid(row=4, column=0, sticky=tk.E)

        user_type = tk.IntVar()

        self.learner_button = tk.Radiobutton(self,
                                             text="Learner",
                                             variable=user_type,
                                             value="Learner",
                                             command=self.disable_parent_child)
        
        self.educator_button = tk.Radiobutton(self,
                                             text="Educator",
                                             variable=user_type,
                                             value="Educator",
                                             command=self.disable_parent_child)
        
        self.parent_button = tk.Radiobutton(self,
                                             text="Parent",
                                             variable=user_type,
                                             value="Parent",
                                             command=self.ask_for_parent_child)

        self.learner_button.grid(row=4, column=1, sticky=tk.W)
        self.educator_button.grid(row=5, column=1, sticky=tk.W)
        self.parent_button.grid(row=6, column=1, sticky=tk.W)

        register_button = tk.Button(self, text="Register", command=self.register)
        register_button.grid(row=8, columnspan=2, pady=50)

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
        self.login_frame.register

