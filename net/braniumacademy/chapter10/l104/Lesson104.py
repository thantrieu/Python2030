# 1. Giới thiệu Entry widget
# 2. Ẩn giấu mật khẩu và thông tin nhạy cảm
# 3. Ví dụ minh họa

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror


class LearnEntry(tk.Tk):
    def __init__(self):
        super().__init__()
        self.email = tk.StringVar()
        self.password = tk.StringVar()
        self.icon = tk.PhotoImage(file='user_24.png')
        self.title('Learn Entry')
        self.geometry('320x140')
        self.configure(padx=16, pady=8)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        label_email = ttk.Label(text='Email: ', padding=4, justify='left')
        label_email.grid(row=0, column=0, ipadx=8, ipady=8, sticky=tk.W)
        entry_email = ttk.Entry(textvariable=self.email)
        entry_email.grid(row=0, column=1, columnspan=2, ipadx=4, ipady=4, sticky=tk.EW)
        label_password = ttk.Label(text='Password: ', padding=4, justify='left')
        label_password.grid(row=1, column=0, ipadx=8, ipady=8, sticky=tk.W)
        entry_password = ttk.Entry(textvariable=self.password, show='*')
        entry_password.grid(row=1, column=1, columnspan=2, ipadx=4, ipady=4, sticky=tk.EW)
        btn_login = ttk.Button(text='Login', command=self.login,
                               image=self.icon, compound='left')
        btn_login.grid(row=2, column=2, sticky=tk.E)

    def login(self):
        email = 'braniumacademy@xmail.com'
        password = '123456@'
        text_email = self.email.get().lower()
        text_password = self.password.get()
        if len(text_password) == 0 or len(text_email) == 0:
            showerror(title='Login Error', message='Email and password cannot be blank!')
        elif text_email != email or text_password != password:
            showerror(title='Login Failed', message="Incorrect email or password!")
        else:
            showinfo(title='Login Success', message='Wecome to Branium Academy!')


if __name__ == '__main__':
    app = LearnEntry()
    app.mainloop()
