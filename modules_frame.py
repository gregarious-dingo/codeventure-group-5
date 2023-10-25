import tkinter as tk
from resources.learning_modules import Learning_Modules
from level_frame import LevelFrame

import tkinter as tk
from resources.learning_modules import Learning_Modules
from level_frame import LevelFrame

class LearningModulesFrame(tk.Frame):
    def __init__(self, master, learner_frame, user):
        super().__init__(master)
        self.learner_frame = learner_frame
        self.user = user
        self.learning_modules = Learning_Modules()
        levels = self.learning_modules.levels

        selection_message = tk.Label(self, text=f'Hi, {user.username}. Please select one of the following modules:')
        selection_message.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky=tk.N)

        row = 1  # Initialize row
        for i in range(0, len(levels), 2):
            level_left = levels[i]
            level_right = levels[i + 1] if i + 1 < len(levels) else None

            # Create frames to hold buttons and adjust their alignment
            left_frame = tk.Frame(self)
            right_frame = tk.Frame(self)

            left_frame.grid(row=row, column=0, padx=35, pady=10, sticky=tk.E)
            right_frame.grid(row=row, column=1, padx=0, pady=10, sticky=tk.W)

            button_left = tk.Button(left_frame, text=level_left.name, 
                                    command=lambda level=level_left: self.select_level(level))
            button_left.pack(side=tk.RIGHT, padx=5)

            if level_right:
                button_right = tk.Button(right_frame, text=level_right.name, 
                                         command=lambda level=level_right: self.select_level(level))
                button_right.pack(side=tk.RIGHT, padx=5)

            row += 1

        back_to_menu_button = tk.Button(self, text="Back to menu", command=self.back_to_menu)
        back_to_menu_button.grid(row=row, column=0, columnspan=2, padx=10, pady=10, sticky=tk.N)

    def back_to_menu(self):
        self.place_forget()
        self.learner_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def select_level(self, level):
        print("clicked")
        self.place_forget()
        level_frame = LevelFrame(self.master, self, level, self.user)
        level_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

