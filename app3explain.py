import tkinter as tk
window = tk.Tk()
window.title('style app')

label = tk.Label(text='hello',font=('Gabriola',25),fg="blue").pack()
label2 = tk.Label(text="welcome to my app",font=('Gabriola',25),fg="blue",bg="black").pack()

window.resizable(0,0)
window.geometry('500x500')
window.configure(bg='yellow')
window.mainloop()
