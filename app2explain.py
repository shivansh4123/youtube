import tkinter as tk
window = tk.Tk()
window.title('Rate us app')
def good():
    ma = tk.Label(text="thank you very much").pack()
def av():
    ma2 = tk.Label(text="thanks for rating").pack()
def bad():
    ma3 = tk.Label(text="we will try to improve").pack()
inrto = tk.Label(text="Welcome to my app").pack()
rate_us = tk.Label(text="Rate us").pack()
button = tk.Button(text="😀",command=good)
button.pack()
button2 = tk.Button(text="😐",command=av)
button2.pack()
button3 = tk.Button(text="🙁",command=bad)
button3.pack()
window.mainloop()
