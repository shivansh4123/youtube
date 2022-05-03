import tkinter as tk
import tkinterweb
window = tk.Tk()
window.title('imaginationsea browser')
def search():
    a = entry.get()
    frame.load_website(f'{a}')

entry = tk.Entry()
entry.pack()
button = tk.Button(text="go",command=search)
button.pack()
frame = tkinterweb.HtmlFrame(window)
frame.load_website('www.google.com')
frame.pack(fill="both", expand=True)

window.mainloop()
