import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Learn Radiobutton')
img = tk.PhotoImage(file='search.png')
root.geometry('360x220')
root.resizable(False, False)
btn = ttk.Button(root, text='Click me', image=img, compound=tk.LEFT)
btn.grid(row=0, column=0)

if __name__ == '__main__':
    root.mainloop()
