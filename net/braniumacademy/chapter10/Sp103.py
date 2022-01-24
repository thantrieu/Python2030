import tkinter as tk
from tkinter import ttk


class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('400x100')
        self.title('Login')
        self.resizable(False, False)
        # root.grid(baseWidth=100, baseHeight=100)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        self.grid(baseWidth=1, baseHeight=1, widthInc=1, heightInc=1)
        self.create_widgets()

    def create_widgets(self):
        # add label
        label_username = ttk.Label(self, text='Username: ')
        label_username.grid(row=0, column=0, sticky=tk.W, pady=4, padx=4)
        label_password = ttk.Label(self, text='Password: ')
        label_password.grid(row=1, column=0, sticky=tk.W, pady=4, padx=4)
        # add entry
        entry_username = ttk.Entry(self)
        entry_username.grid(row=0, column=1, sticky=tk.EW, padx=4, pady=4, ipadx=4, ipady=4)
        entry_password = ttk.Entry(self, show='*')
        entry_password.grid(row=1, column=1, sticky=tk.EW, padx=4, pady=4, ipadx=4, ipady=4)
        # add button
        btn_login = ttk.Button(self, text='Login')
        btn_login.grid(row=3, column=1, sticky=tk.EW, pady=4, padx=4, ipady=4, ipadx=8)


if __name__ == '__main__':
    app = MyApp()
    app.mainloop()
