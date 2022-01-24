# 1. Giới thiệu Label widget
# 2. Cài đặt font cho Label
# 3. Hiển thị ảnh trong label
# 4. Ví dụ minh họa

import tkinter as tk
from tkinter import ttk
from tkinter import font


class LearnLabel(tk.Tk):
    def __init__(self):
        super().__init__()
        self.label = None
        self.icon = tk.PhotoImage(file='correct.png')
        self.title('Learn Label')
        self.geometry('300x200')
        self.configure(padx=16, pady=16)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.myfont = font.Font(family='Arial', size=14)
        self.create_widgets()

    def create_widgets(self):
        self.label = ttk.Label(text='Hello World!',
                               background='red', foreground='white',
                               padding=8, font=self.myfont,
                               image=self.icon, compound=tk.LEFT)
        self.label.grid(row=0, column=0, ipadx=8, ipady=8)
        btn_increment = ttk.Button(text='+', command=self.size_up, padding=8)
        btn_increment.grid(row=1, column=0)
        btn_decrement = ttk.Button(text='-', command=self.size_down, padding=8)
        btn_decrement.grid(row=2, column=0)

    def size_up(self):
        size = self.myfont['size']
        self.myfont.configure(size=size + 2)

    def size_down(self):
        size = self.myfont['size']
        self.myfont.configure(size=size - 2)


if __name__ == '__main__':
    app = LearnLabel()
    app.mainloop()
