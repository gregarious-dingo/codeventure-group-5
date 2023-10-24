import tkinter as tk

class EducatorFrame(tk.Frame):
    def __init__(self, master, login_frame, user):
        super().__init__(master)
        self.login_frame = login_frame

        welcome_message = tk.Label(self, text=f'Welcome {user.username}')
        welcome_message.grid(row=1, columnspan=2, sticky=tk.NW, padx=10, pady=10)

        back_to_login_button = tk.Button(self, text="Log Out", command=self.log_out)
        back_to_login_button.grid(row=10, columnspan=2)

    def log_out(self):
        self.place_forget()
        self.login_frame.place(relx=0.5, rely=0.5, anchor= tk.CENTER)