import tkinter as tk
from resources.learning_modules import Learning_Modules

class LearningModulesFrame(tk.Frame):
    def __init__(self, master, learner_frame, user):
        super().__init__(master)
        self.learner_frame = learner_frame
        self.learning_modules = Learning_Modules()

        selection_message = tk.Label(self, text=f'Hi, {user.username}. Please select one of the following modules.')
        selection_message.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky=tk.N)

        back_to_menu_button = tk.Button(self, text="Back to menu", command=self.back_to_menu)
        back_to_menu_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky=tk.N)


    def back_to_menu(self):
        self.place_forget()
        self.learner_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

