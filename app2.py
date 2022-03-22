import tkinter as tk
import time
window = tk.Tk()
def s():
    great = tk.Label(text="thanks for this excellent support")
    great.pack()
def n():
    great2 = tk.Label(text="thanks for this")
    great2.pack()
def a():
    great3 = tk.Label(text="next time we will do better")
    great3.pack()
hello = tk.Label(text="Hello,i m shivansh seth")
hello.pack()
hello2 = tk.Label(text="what do you think about me")
hello2.pack()
button = tk.Button(text="😀",command=s)
button.pack()
button2 = tk.Button(text="😐",command=n)
button2.pack()
button3 = tk.Button(text="🙁",command=a)
button3.pack()
window.mainloop()
