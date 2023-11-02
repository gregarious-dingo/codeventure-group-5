from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
class cpane(ttk.Frame):
   """
   Helper function imported from the Internet from https://www.geeksforgeeks.org/collapsible-pane-in-tkinter-python/
   A class that when instantiated creates a pane that can be expanded and collapsed
   """
   def __init__(self, MainWindow, expanded_text, collapsed_text):
      ttk.Frame.__init__(self, MainWindow)
      # The class variable
      self.MainWindow = MainWindow
      self._expanded_text = expanded_text
      self._collapsed_text = collapsed_text

      self.columnconfigure(1, weight=1)
      self._variable = tk.IntVar()

      self._button = ttk.Checkbutton(self, variable=self._variable,
      command=self._activate, style="TButton")
      self._button.grid(row=0, column=0)

      self._separator = ttk.Separator(self, orient="horizontal")
      self._separator.grid(row=0, column=1, sticky="we")
      self.frame = ttk.Frame(self)

      self._activate()
   def _activate(self):
      if not self._variable.get():
         # Remove this widget when button pressed.
         self.frame.grid_forget()
         # Show collapsed text
         self._button.configure(text=self._collapsed_text)
      elif self._variable.get():
         # Increase the frame area as needed
         self.frame.grid(row=1, column=0, columnspan=2)
         self._button.configure(text=self._expanded_text)
   def toggle(self):
      self._variable.set(not self._variable.get())
      self._activate()