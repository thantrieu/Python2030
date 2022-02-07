import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showwarning


class CommandBinding(tk.Tk):
    def __init__(self):
        super(CommandBinding, self).__init__()
        self.checkbox_confirm = None
        self.btn_register = None
        self.agree_state = tk.IntVar(value=0)
        self.title('Command Binding')
        self.email = tk.StringVar()
        self.password = tk.StringVar()
        self.configure(padx=16, pady=8)
        self.resizable(False, False)
        self.create_widgets()
        self.register_events()

    def create_widgets(self):
        label_email = ttk.Label(text='Email: ', padding=4, justify='left')
        label_email.grid(row=0, column=0, ipadx=4, ipady=4, sticky=tk.W)
        entry_email = ttk.Entry(textvariable=self.email)
        entry_email.grid(row=0, column=1, columnspan=2, ipadx=4, ipady=4, sticky=tk.EW)
        label_password = ttk.Label(text='Password: ', padding=4, justify='left')
        label_password.grid(row=1, column=0, ipadx=4, ipady=4, sticky=tk.W)
        entry_password = ttk.Entry(textvariable=self.password, show='*')
        entry_password.grid(row=1, column=1, columnspan=2, ipadx=4, ipady=4, sticky=tk.EW)
        self.btn_register = ttk.Button(text='Register', command=self.btn_register_clicked)
        self.btn_register.grid(row=2, column=2, ipadx=4, ipady=4, sticky=tk.E)
        self.checkbox_confirm = ttk.Checkbutton(text='I agree join BA', variable=self.agree_state)
        self.checkbox_confirm.grid(row=2, column=0, sticky=tk.EW)

    def register_events(self):
        self.checkbox_confirm.bind('<Return>', self.user_confirmed)
        self.checkbox_confirm.bind('<a>', self.user_confirmed)
        self.checkbox_confirm.bind('<Escape>', self.user_rejected)
        self.checkbox_confirm.bind('<d>', self.user_rejected)
        self.btn_register.bind('<Return>', self.btn_register_clicked)
        self.checkbox_confirm.bind('<<Confirmed>>', self.user_confirmed)
        self.btn_register.bind('<KeyPress-a>', self.altkey_pressed)
        self.btn_register.bind('<3>', self.altkey_pressed)

    def altkey_pressed(self, event):
        self.checkbox_confirm.event_generate('<<Confirmed>>')

    def btn_register_clicked(self, *event):
        if self.agree_state.get() == 1:
            showinfo('Infomation', 'Welcome to Branium Academy!')
        else:
            showwarning('Attention', 'Please confirm your agreement!')

    def enter_pressed(self, event):
        print('Enter key pressed')

    def right_mouse_clicked(self, event):
        print('Right mouse clicked')

    def right_arrow_key_pressed(self, event):
        print('Right arrow key pressed')

    def user_confirmed(self, event):
        if self.agree_state.get() == 0:
            self.agree_state.set(1)
            print('I confirm!')

    def user_rejected(self, event):
        if self.agree_state.get() == 1:
            self.agree_state.set(0)
            print('I disagree!')


if __name__ == '__main__':
    obj = CommandBinding()
    obj.mainloop()
