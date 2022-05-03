import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title('pop up')
window.geometry("300x200")

label = tk.Label(text="pop up windows are coming", font="50")
label.pack()

tk.messagebox.showinfo("show info", "Information")

tk.messagebox.showwarning("show warnig", "Warning")

tk.messagebox.showerror("showerror", "Error")

tk.messagebox.askquestion("askquestion", "Are you sure?")

tk.messagebox.askokcancel("askokcancel", "Want to continue?")

tk.messagebox.askyesno("askyesno", "Find the value?")

tk.messagebox.askretrycancel("askretrycancel", "Try again?")

window.state('zoomed')
window.mainloop()
