# Tổng quan về toplevel window
# Thiết lập kích thước cho cửa sổ
# Thiết lập biểu tượng cho cửa sổ
# Căn giữa màn hình
# Căn chỉnh thu phóng cửa sổ màn hình
# Chỉnh độ trong suốt của màn hình

import tkinter as tk
from tkinter import ttk


class ToplevelWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('My Toplevel Window')
        width = 400
        height = 300
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        center_x = screen_width//2 - width//2
        center_y = screen_height//2 - height//2
        self.geometry(f'{width}x{height}+{center_x}+{center_y}')
        # self.minsize(width=width, height=height)
        # self.maxsize(width=2*width, height=2*height)
        self.resizable(False, False)
        self.configure(background='#6cafe5', pady=16, padx=16)
        ttk.Button(text='Click Me').grid(row=0, column=0)
        # add icon
        self.iconbitmap('icon.ico')
        # add transparent
        self.attributes('-alpha', 0.85)


app = ToplevelWindow()
app.mainloop()
