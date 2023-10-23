import tkinter as tk
r = tk.Tk()

def disable_all():
    d.destroy()
    for z in (a, b, c):
        z.config(state = 'disabled')

def func(y):
    print('you clicked button ', y)

a = tk.Button(text = 'A', command = lambda: func('a'))
b = tk.Button(text = 'B', command = lambda: func('b'))
c = tk.Button(text = 'C', command = lambda: func('c'))
d = tk.Button(text = 'disable all', command = disable_all)

for x in (a, b, c, d):
    x.pack()

r.mainloop()