import tkinter as tk
from login_frame import LoginFrame

class Interface(tk.Tk):

    def __init__(self, title, width=960, height=540):

        super().__init__()
        self.title = title
        self.geometry(f'{width}x{height}')

    if __name__ == "__main__":
        codeventure = Interface("CodeVenture")
        login = LoginFrame(codeventure)




#example to show how github works
