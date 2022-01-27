# 1. Giới thiệu combobox widget
# 2. Ví dụ minh họa

import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as msgbox
from calendar import month_name, day_name


class LearnCombobox(tk.Tk):
    def __init__(self):
        super().__init__()
        self.result = None
        self.title('Learn Combobox')
        self.geometry('400x200')
        self.configure(pady=16, padx=16)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.selected_day = tk.StringVar()
        self.selected_month = tk.StringVar()
        self.create_frame_day()
        self.create_frame_month()
        self.create_btn_submit()

    def create_btn_submit(self):
        # add button submit
        ttk.Button(text='Sumit', command=self.btn_submit_clicked). \
            grid(row=1, column=0, columnspan=2, padx=4, pady=4, sticky=tk.EW)

    def create_frame_day(self):
        frm = ttk.Labelframe(text='Favorite day of week')
        ttk.Label(frm, text='Select day of week: '). \
            grid(row=0, column=0, padx=4, pady=4, sticky=tk.W)
        # add combobox
        days = self.get_days()
        combobox = ttk.Combobox(frm, values=days, state='readonly',
                                textvariable=self.selected_day)
        combobox.grid(row=1, column=0, pady=4, padx=4, sticky=tk.W)
        # combobox.bind('<<ComboboxSelected>>', self.day_change)
        combobox.current(newindex=0)
        frm.grid(row=0, column=0, sticky=tk.NSEW, pady=4, padx=4)

    def create_frame_month(self):
        frm = ttk.Labelframe(text='Favorite month')
        ttk.Label(frm, text='Select day of week: '). \
            grid(row=0, column=0, padx=4, pady=4, sticky=tk.W)
        # add combobox
        months = self.get_months()
        combobox = ttk.Combobox(frm, values=months, state='readonly',
                                textvariable=self.selected_month)
        combobox.grid(row=1, column=0, pady=4, padx=4, sticky=tk.W)
        # combobox.bind('<<ComboboxSelected>>', self.day_change)
        combobox.current(newindex=1)
        frm.grid(row=0, column=1, sticky=tk.NSEW, pady=4, padx=4)

    def get_months(self):
        months = []
        for m in month_name:
            months.append(m)
        return months

    def get_days(self):
        days = []
        for d in day_name:
            days.append(d)
        return days

    def btn_submit_clicked(self):
        title = 'Result'
        message = f'Day:{self.selected_day.get()}\n' \
                  f'Month: {self.selected_month.get()}'
        msgbox.showinfo(title=title, message=message)

    def day_change(self, *args):
        self.result = self.selected_day.get()


if __name__ == '__main__':
    app = LearnCombobox()
    app.mainloop()
