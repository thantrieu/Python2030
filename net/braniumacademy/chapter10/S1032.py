import tkinter as tk
from tkinter import ttk
from tkinter import font


def size_up():
    size = myfont['size']
    myfont.configure(size=size + 2)


def size_down():
    size = myfont['size']
    myfont.configure(size=size - 2)


root = tk.Tk()
root.title('Learn Label')
root.geometry('300x200')
root.grid_columnconfigure(0, weight=1)
root.configure(padx=8, pady=16)
root.grid_rowconfigure(0, weight=1, pad=16)
root.grid_rowconfigure(1, weight=1, pad=16)
root.grid_rowconfigure(2, weight=1, pad=16)
label = ttk.Label(root, text='Hello World!',
                  background='red', foreground='white', padding=8)
myfont = font.Font(root, family='Arial', size=14)
label.configure(font=myfont)
label.grid(row=0, column=0, ipady=8, ipadx=8)
btn_increment = ttk.Button(text='+', command=size_up, padding=8)
btn_increment.grid(row=1, column=0)
btn_decrement = ttk.Button(text='-', command=size_down, padding=8)
btn_decrement.grid(row=2, column=0)

root.mainloop()
