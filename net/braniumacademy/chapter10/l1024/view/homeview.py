import tkinter as tk
from tkinter import ttk, Menu
from net.braniumacademy.chapter10.l1024.view.addnewstudentview import AddNewStudentView
from net.braniumacademy.chapter10.l1024.view.studentview import StudentView


class HomeView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('QUẢN LÝ ĐĂNG KÝ MÔN HỌC')
        self.resizable(False, False)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.configure(padx=8, pady=8)
        self.menubar = Menu()
        self.configure(menu=self.menubar)
        self.create_notebook()
        self.create_student_view()
        self.create_menu()

    def create_notebook(self):
        notebook = ttk.Notebook()
        notebook.grid(row=0, column=0, sticky=tk.NSEW)
        # add student frame
        self.frm_student = ttk.Frame(notebook)
        self.frm_student.rowconfigure(0, weight=4)
        self.frm_student.rowconfigure(1, weight=1)
        self.frm_student.columnconfigure(0, weight=3)
        self.frm_student.columnconfigure(1, weight=3)
        self.frm_student.columnconfigure(2, weight=3)
        self.frm_student.columnconfigure(3, weight=1)
        self.frm_student.grid(row=0, column=0)
        # add subject frame
        self.frm_subject = ttk.Frame(notebook)
        self.frm_subject.rowconfigure(0, weight=4)
        self.frm_subject.rowconfigure(1, weight=1)
        self.frm_subject.columnconfigure(0, weight=3)
        self.frm_subject.columnconfigure(1, weight=3)
        self.frm_subject.columnconfigure(2, weight=3)
        self.frm_subject.columnconfigure(3, weight=1)
        self.frm_subject.grid(row=0, column=0)
        # add register frame
        self.frm_register = ttk.Frame(notebook)
        self.frm_register.rowconfigure(0, weight=4)
        self.frm_register.rowconfigure(1, weight=1)
        self.frm_register.columnconfigure(0, weight=1)
        self.frm_register.columnconfigure(1, weight=1)
        self.frm_register.columnconfigure(2, weight=1)
        self.frm_register.grid(row=0, column=0)
        # add frame to notebook
        notebook.add(self.frm_student, text='Student Managerment')
        notebook.add(self.frm_subject, text='Subject Managerment')
        notebook.add(self.frm_register, text='Register Managerment')

    def create_menu(self):
        file_menu = Menu(self.menubar, tearoff=False)
        file_menu.add_command(label='Create New Student', underline=0,
                              command=lambda: self.create_student())
        # find by submenu
        submenu_find_by = Menu(file_menu, tearoff=False)
        submenu_find_by.add_command(label='By Name')
        submenu_find_by.add_command(label='By GPA')
        submenu_find_by.add_command(label='By Birth Day')
        submenu_find_by.add_command(label='By Birth Month')
        submenu_find_by.add_command(label='By Birth Year')
        file_menu.add_cascade(label='Find...', menu=submenu_find_by)
        # sort by submenu
        submenu_sort_by = Menu(file_menu, tearoff=False)
        submenu_sort_by.add_command(label='By Name Increment',
                                    command=lambda: self.student_view.sort_by_name())
        submenu_sort_by.add_command(label='By Birthdate Increment',
                                    command=lambda: self.student_view.sort_by_birth_date())
        submenu_sort_by.add_command(label='By GPA Decrement',
                                    command=lambda: self.student_view.sort_by_gpa())
        submenu_sort_by.add_command(label='By GPA Decrement & Name Increment',
                                    command=lambda: self.student_view.sort_by_gpa_and_name())
        file_menu.add_cascade(label='Sort...', menu=submenu_sort_by)
        # save menu item
        file_menu.add_command(label='Save', command=lambda : self.save())
        # other menu items
        file_menu.add_separator()
        file_menu.add_command(label='Exit', underline=0, command=self.destroy)
        # add to menu bar
        self.menubar.add_cascade(label='File', menu=file_menu, underline=0)

    def create_student_view(self):
        self.student_view = StudentView(self.frm_student)

    def create_student(self):
        popup = AddNewStudentView(self.student_view)
        popup.attributes('-topmost', True)  # showing popup alway on top of master frame
        popup.mainloop()

    def save(self):
        self.student_view.save()
