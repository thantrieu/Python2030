import tkinter
from tkinter import ttk
from tkinter.messagebox import showinfo, askyesno, showerror

from net.braniumacademy.chapter10.l1024.controller.studentcontroller import StudentController
from net.braniumacademy.chapter10.l1024.error.exceptions import GpaError


class EditStudentView(tkinter.Tk):
    def __init__(self, master, student):
        super(EditStudentView, self).__init__()
        self.master = master
        self.student = student
        self.resizable(False, False)
        self.title('Edit GPA')
        self.create_widgets()

    def create_widgets(self):
        self.entry_student_id = ttk.Entry(self)
        self.entry_full_name = ttk.Entry(self)
        self.entry_gpa = ttk.Entry(self)
        # insert text
        self.entry_student_id.insert(0, str(self.student.student_id))
        self.entry_full_name.insert(0, str(self.student.full_name))
        self.entry_gpa.insert(0, str(self.student.gpa))
        # disable all entry but gpa entry
        self.entry_full_name.configure(state='disabled')
        self.entry_student_id.configure(state='disabled')
        # add button
        self.btn_cancel = ttk.Button(self, text='Cancel', command=self.destroy)
        self.btn_save = ttk.Button(self, text='Save', command=lambda: self.check_error())
        # add label
        ttk.Label(self, text='Mã SV:').grid(row=0, column=0, padx=4, pady=2)
        ttk.Label(self, text='Họ và tên:').grid(row=1, column=0, padx=4, pady=2)
        ttk.Label(self, text='Điểm TB:').grid(row=2, column=0, padx=4, pady=2)
        # put into grid
        self.entry_student_id.grid(row=0, column=1, pady=2, padx=4)
        self.entry_full_name.grid(row=1, column=1, pady=2, padx=4)
        self.entry_gpa.grid(row=2, column=1, pady=2, padx=4)
        self.btn_save.grid(row=3, column=1, pady=4, padx=4)
        self.btn_cancel.grid(row=3, column=0, pady=4, padx=4)

    def check_error(self):
        controller = StudentController()
        gpa = float(self.entry_gpa.get())
        ans = askyesno('Confirmation', 'Bạn có chắc muốn lưu các thay đổi?')
        if ans:
            try:
                controller.edit(student=self.student, gpa=gpa)
                self.master.show_students()
                showinfo('Completion', message='Update student\'s GPA successfully!')
                self.destroy()
            except GpaError as e:
                showerror('GPA Error', message=e.__str__())
                self.destroy()
