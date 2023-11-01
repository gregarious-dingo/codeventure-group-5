import tkinter as tk
from progress_tracker_frame import ProgressTrackerFrame

class ParentFrame(tk.Frame):
    def __init__(self, master, login_frame, user):
        super().__init__(master)
        self.login_frame = login_frame
        self.user = user
        self.learner = user.learner

        welcome_message = tk.Label(self, text=f'Welcome, {user.username}!')
        welcome_message.grid(row=0, columnspan=2, sticky=tk.N, padx=10, pady=10)

        progress_button = tk.Button(self, text=f"Check {self.learner.username}'s progress", 
                                    command=self.check_progress)
        progress_button.grid(row=1, columnspan=2, sticky=tk.N, padx=10, pady=10)

        toggle_button_text = ""
        if not self.learner_is_blocked():
            toggle_button_text = f"Block {self.learner.username}'s Account"
        else:
            toggle_button_text = f"Unblock {self.learner.username}'s Account"
        self.toggle_block_button = tk.Button(self, text=toggle_button_text, command=self.toggle_block)
        self.toggle_block_button.grid(row=2, columnspan=2, sticky=tk.N, padx=10, pady=10)

        logout_button = tk.Button(self, text="Log Out", command=self.log_out)
        logout_button.grid(row=10, columnspan=2, padx=10, pady=10)

    def log_out(self):
        self.place_forget()
        self.login_frame.place(relx=0.5, rely=0.5, anchor= tk.CENTER)

    def check_progress(self):
        self.place_forget()
        learner_progress_frame = ProgressTrackerFrame(self.master, self, self.learner, True, False)
        learner_progress_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def toggle_block(self):
        if not self.learner_is_blocked():
            self.toggle_block_button["text"] = f"Unblock {self.learner.username}'s Account"
            self.user.block_learner()
        else:
            self.toggle_block_button["text"] = f"Block {self.learner.username}'s Account"
            self.user.unblock_learner()

    def learner_is_blocked(self):
        if self.learner.blocked:
            return True
        else:
            return False
