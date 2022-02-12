import tkinter
from tkinter import ttk
from tkinter.messagebox import showerror

from net.braniumacademy.chapter10.l1024.controller.studentcontroller import StudentController
from net.braniumacademy.chapter10.l1024.error.exceptions import NameInvalidError, BirthdateError


class StudentPopup(tkinter.Tk):
    def __init__(self, master):
        super(StudentPopup, self).__init__()
        self.master = master
        self.resizable(False, False)
        self.title('Add New Student Popup')
        self.create_widgets()

    def create_widgets(self):
        self.entry_person_id = ttk.Entry(self)
        self.entry_full_name = ttk.Entry(self)
        self.entry_email = ttk.Entry(self)
        self.entry_gpa = ttk.Entry(self)
        self.entry_major = ttk.Entry(self)
        self.entry_birth_date = ttk.Entry(self)
        # add button
        self.btn_cancel = ttk.Button(self, text='Cancel', command=self.destroy)
        self.btn_add = ttk.Button(self, text='Add', command=lambda: self.check_error())
        # add label
        ttk.Label(self, text='CMND/CCCD:').grid(row=0, column=0, padx=4, pady=2)
        ttk.Label(self, text='Họ và tên:').grid(row=1, column=0, padx=4, pady=2)
        ttk.Label(self, text='Ngày sinh:').grid(row=2, column=0, padx=4, pady=2)
        ttk.Label(self, text='Email:').grid(row=3, column=0, padx=4, pady=2)
        ttk.Label(self, text='Điểm TB:').grid(row=4, column=0, padx=4, pady=2)
        ttk.Label(self, text='Chuyên ngành:').grid(row=5, column=0, padx=4, pady=2)
        # put into grid
        self.entry_person_id.grid(row=0, column=1, pady=2, padx=4)
        self.entry_full_name.grid(row=1, column=1, pady=2, padx=4)
        self.entry_birth_date.grid(row=2, column=1, pady=2, padx=4)
        self.entry_email.grid(row=3, column=1, pady=2, padx=4)
        self.entry_gpa.grid(row=4, column=1, pady=2, padx=4)
        self.entry_major.grid(row=5, column=1, pady=2, padx=4)
        self.btn_add.grid(row=6, column=1, pady=4, padx=4)
        self.btn_cancel.grid(row=6, column=0, pady=4, padx=4)

    def check_error(self):
        controller = StudentController()
        person_id = self.entry_person_id.get()
        full_name = self.entry_full_name.get()
        birth_date = self.entry_birth_date.get()
        email = self.entry_email.get()
        gpa_str = self.entry_gpa.get()
        major = self.entry_major.get()
        if person_id == '':
            showerror('Person ID Error', message='Person id cannot be blank.')
            raise Exception()
        try:
            controller.check_name_valid(full_name)
        except NameInvalidError as e:
            showerror('NameInvalidError', message=e.__str__())
        try:
            controller.check_birth_date_valid(birth_date)
        except BirthdateError as e:
            showerror('BirthdateError', message=e.__str__())
        self.master.create_student()
