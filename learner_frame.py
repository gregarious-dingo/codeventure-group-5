import tkinter as tk
from modules_frame import LearningModulesFrame
from progress_tracker_frame import ProgressTrackerFrame

class LearnerFrame(tk.Frame):
    def __init__(self, master, login_frame, user):
        super().__init__(master)
        self.login_frame = login_frame
        self.user = user

        welcome_message = tk.Label(self, text=f'Welcome {user.username}!')
        welcome_message.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky=tk.N)

        if not self.user.blocked:
            select_learning_module_button = tk.Button(self, text="Select a Learning Module", 
                                                      command=self.select_learning_module)
            select_learning_module_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky=tk.N)

            check_progress_button = tk.Button(self, text="Check Progress", command=self.check_progress)
            check_progress_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky=tk.N)

        else:
            blocked_message = tk.Label(self, text='Your account is currently blocked!\n'
                                                'Looks like someone has been spending too much time on their computer...')
            blocked_message.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")


        logout_button = tk.Button(self, text="Log Out", command=self.log_out)
        logout_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky=tk.N)

    def log_out(self):
        self.place_forget()
        self.login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def select_learning_module(self):
        self.place_forget()
        learning_modules_frame = LearningModulesFrame(self.master, self, self.user)
        learning_modules_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def check_progress(self):
        self.place_forget()
        progress_tracker_frame = ProgressTrackerFrame(self.master, self, self.user, False)
        progress_tracker_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
