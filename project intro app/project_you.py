import tkinter as tk
from tkinter.ttk import *
from tkinter import messagebox
from PIL import Image, ImageTk
import webbrowser
window = tk.Tk()
window.geometry('300x300')
window.title('intro application')

def address():
    tk.messagebox.showinfo("show info", "i can not give my full address because it is private")
    
def phone():
    tk.messagebox.showinfo("show info", "i can not give my full phone because it is private")

def youtube():
    webbrowser.open('https://www.youtube.com/channel/UCnTTumtBdkL2N8BzRc9gqRg')

menubar = tk.Menu(window)

file = tk.Menu(menubar, tearoff = 0)
menubar.add_cascade(label='incomplete address', menu = file)
file.add_command(label='click here', command=address)

edit = tk.Menu(menubar, tearoff = 0)
menubar.add_cascade(label='incomplete number', menu = edit)
edit.add_command(label='click here', command=phone)


image1 = Image.open("unnamed.jpg")
test = ImageTk.PhotoImage(image1)

label1 = tk.Label(image=test)
label1.image = test

label1.place(x=200, y=30)

label = tk.Label(text="Name: shivansh seth",font=("Arial", 15),fg="black",bg="light blue")
label.place(x=0,y=0)

label2 = tk.Label(text="Address: XYZ india",font=("Arial", 15),fg="black",bg="light blue")
label2.place(x=0,y=35)

label3 = tk.Label(text="Phone: 9136..",font=("Arial", 15),fg="black",bg="light blue")
label3.place(x=0,y=70)

a = """Language known:-
1.Python
2.HTML/Css
3.Js
"""
label4 = tk.Label(text=a,font=("Arial", 15),fg="black",bg="light blue")
label4.place(x=0,y=105)

button = tk.Button(text="YouTube",command=youtube)
button.place(x=0,y=270)

window.resizable(0,0)
window.config(bg = "light blue",menu = menubar)
window.mainloop()
