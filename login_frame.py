import tkinter as tk
from controllers.login_system import LoginSystem
from users.learner import Learner
from users.educator import Educator
from users.parent import Parent
from register_frame import RegisterFrame
from learner_frame import LearnerFrame
from educator_frame import EducatorFrame
from parent_frame import ParentFrame

class LoginFrame(tk.Frame):

    def __init__(self, master):
        super().__init__(master=master)
        self.master = master
        self.login_system = LoginSystem()
        self.login_system.load_users()

        login_canvas = tk.Canvas(master=self, width=128, height=128)
        login_canvas = login_canvas.grid(row=0, columnspan=2, sticky=tk.S, padx=10, pady=10)

        login_title = tk.Label(master=self,
                                text="Welcome to CodeVenture",
                                font=("Arial Bold", 25))
        login_title.grid(row=1, columnspan=2, padx=10, pady=10)

        username_label = tk.Label(master=self, text="Username:")
        username_label.grid(row=2, column=0, sticky=tk.E, padx=10, pady=10)

        self.username = tk.StringVar()
        self.username_entry = tk.Entry(master=self, textvariable=self.username)
        self.username_entry.grid(row=2, column=1, sticky=tk.W, padx=10, pady=10)

        password_label = tk.Label(master=self, text="Password:")
        password_label.grid(row=3, column=0, sticky=tk.E, padx=10, pady=10)

        self.password = tk.StringVar()
        self.password_entry = tk.Entry(master=self, textvariable=self.password,
                                    show="●")
        self.password_entry.grid(row=3, column=1, sticky=tk.W, padx=10, pady=10)

        login_button = tk.Button(master=self, text="Login",
                                    command=self.authenticate_login)
        login_button.grid(row=4, columnspan=2, padx=10, pady=10)

        self.login_text = tk.StringVar()
        self.login_message = tk.Label(master=self, textvariable=self.login_text)
        self.login_message.grid(row=5, columnspan=2, padx=10, pady=10)

        register_button = tk.Button(master=self, text="Register new account",
                                    command = self.place_register_frame)
        register_button.grid(row=6, columnspan=2, padx=10, pady=10)
        
    def place_register_frame(self):
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.place_forget()

        register_frame = RegisterFrame(self.master, self)
        register_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    
    def authenticate_login(self):
        
        user = self.login_system.authenticate_user_login(self.username_entry.get(), self.password_entry.get())

        if user != False:

            self.username_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)

            if isinstance(user, Learner):
                self.place_forget()

                learner_frame = LearnerFrame(self.master, self, user)
                learner_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
            
            elif isinstance(user, Educator):
                self.place_forget()

                educator_frame = EducatorFrame(self.master, self, user)
                educator_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

            elif isinstance(user, Parent):
                self.place_forget()

                parent_frame = ParentFrame(self.master, self, user)
                parent_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        else:
            self.login_text.set("Incorrect email or password.")

