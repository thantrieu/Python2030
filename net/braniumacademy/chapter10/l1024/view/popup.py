import tkinter
from tkinter import ttk


class StudentPopup(tkinter.Tk):
    def __init__(self):
        super(StudentPopup, self).__init__()
        self.resizable(False, False)
        self.title('Add New Student Popup')
        self.create_widgets()

    def create_widgets(self):
        self.entry_person_id = ttk.Entry()
        self.entry_full_name = ttk.Entry()
        self.entry_email = ttk.Entry()
        self.entry_age = ttk.Entry()
        self.btn_cancel = ttk.Button(text='Cancel')
        self.btn_add = ttk.Button(text='Add')
        # put into grid
        self.entry_person_id.grid(row=0, column=1)
        self.entry_full_name.grid(row=1, column=1)
        self.entry_email.grid(row=2, column=1)
        self.entry_age.grid(row=3, column=1)
        self.btn_add.grid(row=4, column=1)
        self.btn_cancel.grid(row=4, column=0)
