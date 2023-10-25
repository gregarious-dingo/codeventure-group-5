import tkinter as tk

class LevelFrame(tk.Frame):
    def __init__(self, master, modules_frame, level, user):
        super().__init__(master)
        self.modules_frame = modules_frame
        
        selection_message = tk.Label(self, text=f'{level.name}')
        selection_message.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky=tk.N)

        select_another_button = tk.Button(self, text="Go back", command=self.select_another_module)
        select_another_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky=tk.N)

    def select_another_module(self):
        self.place_forget()
        self.modules_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)