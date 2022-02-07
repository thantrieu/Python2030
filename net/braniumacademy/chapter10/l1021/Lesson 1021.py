# 1. Giới thiệu về events binding
# 2. Ví dụ minh họa
# 3. Cấp độ binding
# 4. Unbinding events
# 5. Sự kiện ảo do người dùng tự định nghĩa
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showwarning


class LearnBindingEvent(tk.Tk):
    def __init__(self):
        super(LearnBindingEvent, self).__init__()
        self.title('Events Binding')
        self.agree_state = tk.IntVar(value=0)
        self.email = tk.StringVar()
        self.password = tk.StringVar()
        self.configure(padx=16, pady=8)
        self.resizable(False, False)
        self.create_widgets()
        self.register_events()

    def create_widgets(self):
        ttk.Label(text='Email: ', padding=4, justify='left'). \
            grid(row=0, column=0, ipadx=4, ipady=4, sticky=tk.W)
        self.entry_email = ttk.Entry(textvariable=self.email)
        self.entry_email.grid(row=0, column=1, columnspan=2, ipady=4, ipadx=4)
        # add password
        ttk.Label(text='Password: ', padding=4, justify='left'). \
            grid(row=1, column=0, ipadx=4, ipady=4, sticky=tk.W)
        self.entry_password = ttk.Entry(textvariable=self.email, show='*')
        self.entry_password.grid(row=1, column=1, columnspan=2, ipady=4, ipadx=4)
        # add checkbox
        self.checkbox_confirm = ttk.Checkbutton(text='I agree join BA', variable=self.agree_state)
        self.checkbox_confirm.grid(row=2, column=0, sticky=tk.W)
        # add register button
        self.btn_register = ttk.Button(text='Register', command=self.btn_register_clicked)
        self.btn_register.grid(row=2, column=2, ipadx=4, ipady=4, sticky=tk.E)

    def register_events(self):
        self.btn_register.bind('<Return>', self.btn_register_clicked)
        self.checkbox_confirm.bind('<Return>', self.user_confirmed)
        self.checkbox_confirm.bind('<KeyPress-a>', self.user_confirmed)
        self.checkbox_confirm.bind('<Escape>', self.user_rejected)
        self.checkbox_confirm.bind('<d>', self.user_rejected)
        # bind custom event to a function
        self.checkbox_confirm.bind('<<Confirmed>>', self.user_confirmed)
        # generate event
        self.btn_register.bind('<a>', self.generate_user_event)
        # add binding event for root window
        # self.bind('<Return>', self.raised_event)
        # hủy liên kết tới sự kiện nhấn phím enter trên object checkbox_confirm
        # self.checkbox_confirm.unbind('<Return>')
        # self.bind_class('Button', 'Return', callback)

    def generate_user_event(self, event):
        self.checkbox_confirm.event_generate('<<Confirmed>>')

    def raised_event(self, event):
        print('Root window event binding')

    def user_confirmed(self, event):
        if self.agree_state.get() == 0:
            self.agree_state.set(1)

    def user_rejected(self, event):
        if self.agree_state.get() == 1:
            self.agree_state.set(0)

    def btn_register_clicked(self, *event):
        if self.agree_state.get() == 1:
            showinfo('Infomation', 'Welcome to Branium Academy!')
        else:
            showwarning('Attention', 'Please confirm your agreement!')


if __name__ == '__main__':
    obj = LearnBindingEvent()
    obj.mainloop()
