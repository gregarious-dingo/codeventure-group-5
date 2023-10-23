from login_system import LoginSystem

class LoginFrame(tk.Frame):

    def __init__(self, master):
        super().__init__(master=master)
        self.master = master
        self.login_system = LoginSystem()
        self.login_system.load_users()

        login_canvas = tk.Canvas(master=self, width=128, height=128)
        login_canvas = login_canvas.grid(row=0, columnspan=2, sticky=tk.S, padx=10, pady=10)

        login_title = tk.Label(master=self,
                                text="Welcome to Health "
                                    "Clinic Management System",
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
                                    command=self.login_system.authenticate_user_login)
        login_button.grid(row=4, columnspan=2, padx=10, pady=10)

        self.login_text = tk.StringVar()
        login_message = tk.Label(master=self, textvariable=self.login_text)
        login_message.grid(row=5, columnspan=2, padx=10, pady=10)
        
        #test