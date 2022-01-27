# 1. Giới thiệu listbox widget
# 2. Ví dụ minh họa

import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as msgbox
from calendar import month_name


class LearnListbox(tk.Tk):
    def __init__(self):
        super(LearnListbox, self).__init__()
        self.listbox = None
        self.title('Learn Listbox Widget')
        self.geometry('300x250')
        self.configure(padx=16, pady=16)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.months = tk.StringVar(value=self.get_months())
        self.result = []
        self.create_widgets()

    def create_widgets(self):
        frm = ttk.Labelframe(text='Favorite Month')
        ttk.Label(frm, text='Select your favorite month: '). \
            grid(row=0, column=0, pady=4, padx=4, sticky=tk.W)
        self.listbox = tk.Listbox(frm, listvariable=self.months,
                                  selectmode='extended', height=6)
        self.listbox.grid(row=1, column=0, padx=4, pady=4, sticky=tk.W)
        self.listbox.bind('<<ListboxSelect>>', self.listbox_selected)
        # add submit button
        ttk.Button(text='Submit', command=self.btn_submit_clicked). \
            grid(row=1, column=0, pady=4, padx=4)
        frm.grid(row=0, column=0)

    def listbox_selected(self, event):
        self.result.clear()
        for i in self.listbox.curselection():
            self.result.append(self.listbox.get(i))

    def btn_submit_clicked(self):
        title = 'Result'
        message = ''
        for item in self.result:
            message += item + '\n'
        msgbox.showinfo(title, message)

    def get_months(self):
        months = []
        for m in month_name:
            months.append(m)
        return tuple(months)


if __name__ == '__main__':
    app = LearnListbox()
    app.mainloop()
