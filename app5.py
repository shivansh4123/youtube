import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from time import strftime

window = tk.Tk()
window.title('Notepad')

text = tk.Text()
text.pack(fill="both", expand=True)

menubar = tk.Menu(window)

file = tk.Menu(menubar, tearoff = 0)
menubar.add_cascade(label='File', menu = file)
file.add_command(label='Open', command=None)
file.add_command(label='Save', command=None)
file.add_command(label='New', command=None)

edit = tk.Menu(menubar, tearoff = 0)
menubar.add_cascade(label='Edit', menu = edit)
edit.add_command(label='Cut', command=None)
edit.add_command(label='Copy', command=None)
edit.add_command(label='Paste', command=None)

help_ = tk.Menu(menubar, tearoff = 0)
menubar.add_cascade(label='Help', menu = help_)
help_.add_command(label='about this notepad', command=None)

window.state('zoomed')
window.config(menu = menubar)
window.mainloop()
