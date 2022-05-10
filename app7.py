import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()

image1 = Image.open("main.png")
test = ImageTk.PhotoImage(image1)

image = tk.Label(image=test)
image.image = test

image.place(x=0,y=0)

window.mainloop()
