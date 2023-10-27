import tkinter as tk

class LevelFrame(tk.Frame):
    def __init__(self, master, modules_frame, level, material_index, user):
        super().__init__(master)
        self.modules_frame = modules_frame
        self.level = level
        self.material_index = material_index
        self.user = user
        
        if material_index != len(level.learning_materials):
            level_name_message = tk.Label(self, text=f'{level.name}')
            level_name_message.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky=tk.N)

            level_material_message = tk.Label(self, text=f'{level.learning_materials[material_index]}')
            level_material_message.grid(row=1, column=0, columnspan=2, padx=10, pady=40, sticky=tk.N)

            if material_index > 0:
                prev_button = tk.Button(self, text="Previous", command=self.previous)
                prev_button.grid(row=2, column=0, padx=20, pady=10, sticky=tk.E)
            
            continue_button = tk.Button(self, text="Continue", command=self.continue_level)
            continue_button.grid(row=2, column=1, padx=20, pady=10, sticky=tk.W)
        else:
            level_material_message = tk.Label(self, text=f'tada')
            level_material_message.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky=tk.N)

        select_another_button = tk.Button(self, text="Select another module", command=self.select_another_module)
        select_another_button.grid(row=3, column=0, columnspan=2, padx=10, pady=30, sticky=tk.N)

    def select_another_module(self):
        self.place_forget()
        self.modules_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def previous(self):
        self.place_forget()
        prev_level_frame = LevelFrame(self.master, self.modules_frame, self.level, self.material_index - 1, self.user)
        prev_level_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def continue_level(self):
        self.place_forget()
        next_level_frame = LevelFrame(self.master, self.modules_frame, self.level, self.material_index + 1, self.user)
        next_level_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)