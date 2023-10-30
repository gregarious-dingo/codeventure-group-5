import tkinter as tk
from progress_tracker_frame import ProgressTrackerFrame

class ParentFrame(tk.Frame):
    def __init__(self, master, login_frame, user):
        super().__init__(master)
        self.login_frame = login_frame
        self.user = user

        welcome_message = tk.Label(self, text=f'Welcome {user.username}')
        welcome_message.grid(row=1, columnspan=2, sticky=tk.N, padx=10, pady=10)

        check_child_progress_button = tk.Button(self,
                                                text="Check your child's progress",
                                                padx=10,
                                                pady=10,
                                                command=self.check_child_progress)
        check_child_progress_button.grid(row=3, column=0)


        block_access_button = tk.Button(self,
                                        text="Block your child's access",
                                        padx=10,
                                        pady=10,
                                        command=self.block_access)
        block_access_button.grid(row=4, column=0)

        unblock_access_button = tk.Button(self,
                                          text="Unblock your child's access",
                                          padx=10,
                                          pady=10,
                                          command=self.unblock_access)
        unblock_access_button.grid(row=5, column=0)

        
        self.message = tk.StringVar()
        text_message = tk.Label(self, textvariable= self.message)
        text_message.grid(row=8, column=0)

        back_to_login_button = tk.Button(self, text="Log Out", command=self.log_out)
        back_to_login_button.grid(row=10, columnspan=2)

    def log_out(self):
        self.place_forget()
        self.login_frame.place(relx=0.5, rely=0.5, anchor= tk.CENTER)

    def check_child_progress(self):
        self.place_forget()

        child_progress = ProgressTrackerFrame(self.master, self, self.user.learner)
        child_progress.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def block_access(self):
        self.user.block_learner()
        self.message.set("Blocked your child's access")

    def unblock_access(self):
        self.user.unblock_learner()
        self.message.set("Unblocked your child's access")