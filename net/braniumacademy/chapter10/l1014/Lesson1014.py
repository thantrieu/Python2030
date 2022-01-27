import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as msgbox
from calendar import month_name, day_name


class LearnCombobox(tk.Tk):
    def __init__(self):
        super(LearnCombobox, self).__init__()
        self.title('Learn Combobox')
        self.geometry('400x200')
        self.configure(padx=16, pady=16)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.selected_day = tk.StringVar()
        self.selected_month = tk.StringVar()
        self.create_frame_day()
        self.create_frame_month()
        self.create_submit_button()

    def create_frame_day(self):
        frm = ttk.Labelframe(text='Favorite day of week')
        ttk.Label(frm, text='Select day of week: '). \
            grid(row=0, column=0, sticky=tk.W, padx=4, pady=4)
        days = self.get_days()
        combobox = ttk.Combobox(frm, values=days, state='readonly',
                                textvariable=self.selected_day)
        combobox.grid(row=1, column=0, pady=4, padx=4, sticky=tk.W)
        # setup default selected item
        combobox.current(0)
        frm.grid(row=0, column=0, sticky=tk.NSEW, pady=4, padx=4)

    def create_frame_month(self):
        frm = ttk.Labelframe(text='Favorite month')
        ttk.Label(frm, text='Select month: '). \
            grid(row=0, column=0, sticky=tk.W, padx=4, pady=4)
        month = self.get_month()
        combobox = ttk.Combobox(frm, values=month, state='readonly',
                                textvariable=self.selected_month, height=6)
        combobox.grid(row=1, column=0, pady=4, padx=4, sticky=tk.W)
        # setup default selected item
        combobox.current(1)
        # bind event
        combobox.bind('<<ComboboxSelected>>', self.combobox_selected)
        frm.grid(row=0, column=1, sticky=tk.NSEW, pady=4, padx=4)

    def create_submit_button(self):
        ttk.Button(text='Submit', command=self.btn_submit_clicked). \
            grid(row=1, column=0, columnspan=2, padx=4, pady=4, sticky=tk.EW)

    def get_days(self):
        days = []
        for d in day_name:
            days.append(d)
        return days

    def get_month(self):
        months = []
        for m in month_name:
            months.append(m)
        return months

    def btn_submit_clicked(self):
        title = 'Result'
        message = f'Day: {self.selected_day.get()}\n' \
                  f'Month: {self.selected_month.get()}'
        msgbox.showinfo(title, message)

    def combobox_selected(self, event):
        print(f'Selected month: {self.selected_month.get()}')


if __name__ == '__main__':
    app = LearnCombobox()
    app.mainloop()
