import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showinfo, showwarning


class LearnMessageBox(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Learn MessageBox')
        self.geometry('300x200')
        self.configure(padx=16, pady=16, background='#6caf50')
        self.columnconfigure(0, weight=1)
        self.iconbitmap('../icon.ico')
        self.create_widgets()

    def create_widgets(self):
        ttk.Button(text='Show infomation message', command=self.show_info). \
            grid(row=0, column=0, pady=4, padx=4, sticky=tk.EW)
        ttk.Button(text='Show warning message', command=self.show_warning). \
            grid(row=1, column=0, pady=4, padx=4, sticky=tk.EW)
        ttk.Button(text='Show error message', command=self.show_error). \
            grid(row=2, column=0, pady=4, padx=4, sticky=tk.EW)

    def show_info(self):
        showinfo(title='Infomation', message='Update success!')

    def show_warning(self):
        showwarning(title='Warning', message='This record was existed.')

    def show_error(self):
        showerror(title='Error', message='Your database unreachable.')


if __name__ == '__main__':
    app = LearnMessageBox()
    app.mainloop()
