# 1. Giới thiệu listbox widget
# 2. Ví dụ minh họa

import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as msgbox
from calendar import month_name, day_name


class LearnCombobox(tk.Tk):
    def __init__(self):
        super().__init__()
        self.result = []
        self.title('Learn Confirm Dialog')
        self.geometry('400x250')
        self.configure(pady=16, padx=16)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.selected_month = tk.StringVar(value=self.get_months())
        self.create_frame_month()
        self.create_btn_submit()

    def create_btn_submit(self):
        # add button submit
        ttk.Button(text='Sumit', command=self.btn_submit_clicked). \
            grid(row=1, column=0, columnspan=2, padx=4, pady=4, sticky=tk.EW)

    def create_frame_month(self):
        frm = ttk.Labelframe(text='Favorite month')
        ttk.Label(frm, text='Select your favorite month: '). \
            grid(row=0, column=0, padx=4, pady=4, sticky=tk.W)
        # add listbox
        self.month_listbox = tk.Listbox(frm, listvariable=self.selected_month,
                                        selectmode='extended', height=6)
        self.month_listbox.grid(row=1, column=0, pady=4, padx=4, sticky=tk.W)

        self.month_listbox.bind('<<ListboxSelect>>', self.month_selected)
        frm.grid(row=0, column=0, pady=4, padx=4)

    def get_months(self):
        months = []
        for m in month_name:
            months.append(m)
        return tuple(months)

    def btn_submit_clicked(self):
        title = 'Result'
        message = ''
        for item in self.result:
            message += item + '\n'
        msgbox.showinfo(title=title, message=message)

    def month_selected(self, event):
        self.result.clear()
        for i in self.month_listbox.curselection():
            self.result.append(self.month_listbox.get(i))


if __name__ == '__main__':
    app = LearnCombobox()
    app.mainloop()
