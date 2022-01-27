import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showwarning, showerror


class LearnMessageBox(tk.Tk):
    def __init__(self):
        super(LearnMessageBox, self).__init__()
        self.title('Learn MessageBox')
        self.geometry('300x200')
        self.configure(padx=16, pady=16, background='#6caf50')
        self.columnconfigure(0, weight=1)
        self.iconbitmap('../icon.ico')
        self.create_widgets()

    def create_widgets(self):
        ttk.Button(text='Show infomation message', command=self.showinfo). \
            grid(row=0, column=0, pady=4, padx=4, sticky=tk.EW)
        ttk.Button(text='Show warning message', command=self.showwarning). \
            grid(row=1, column=0, pady=4, padx=4, sticky=tk.EW)
        ttk.Button(text='Show error message', command=self.showerror). \
            grid(row=2, column=0, pady=4, padx=4, sticky=tk.EW)

    def showinfo(self):
        showinfo(title='Infomation', message='Update success!')

    def showwarning(self):
        showwarning(title='Warning', message='This record existed')

    def showerror(self):
        showerror(title='Error', message='Your database connection failed.')


if __name__ == '__main__':
    app = LearnMessageBox()
    app.mainloop()
