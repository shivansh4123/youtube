import tkinter as tk
from time import strftime
window = tk.Tk()
window.title('clock')

def time():
	string = strftime('%H:%M:%S %p')
	label.config(text = string)
	label.after(1000, time)

label = tk.Label(font=('calibri',70,'bold'),fg='white',bg='purple')
label.pack()

time()

window.mainloop()
