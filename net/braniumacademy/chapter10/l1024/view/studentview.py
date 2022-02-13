import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, askyesno, showinfo
from net.braniumacademy.chapter10.l1024.utils import *
from net.braniumacademy.chapter10.l1024.controller.studentcontroller import StudentController
from net.braniumacademy.chapter10.l1024.view.editstudentview import EditStudentView


class StudentView:
    def __init__(self, frame):
        super().__init__()
        self.tbl_student = None
        self.frame = frame
        self.students = []
        self.controller = StudentController()
        self.create_widgets()
        self.load_student()

    def create_widgets(self):
        columns = ('id', 'full_name', 'birth_date', 'student_id', 'email', 'gpa', 'major')
        self.tbl_student = ttk.Treeview(self.frame, columns=columns, show='headings', height=10)
        self.tbl_student.grid(row=0, column=0, columnspan=3, sticky=tk.NSEW, pady=4, padx=4)
        style = ttk.Style()
        style.theme_use('alt')  # other theme can use: clam, classic, default
        style.configure('my.Treeview.Heading', font=('Calibri', 11, 'bold'),
                        background='#6caf50', foreground='#ffffff')
        self.tbl_student.configure(style='my.Treeview')
        # customize style for odd and even row background color
        self.tbl_student.tag_configure('odd', background='#f0f0f0')
        self.tbl_student.tag_configure('even', background='#ffffff')
        # show heading
        self.tbl_student.heading('id', text='CMND/CCCD')
        self.tbl_student.heading('full_name', text='Họ và tên')
        self.tbl_student.heading('birth_date', text='Ngày sinh')
        self.tbl_student.heading('student_id', text='Mã SV')
        self.tbl_student.heading('email', text='Email')
        self.tbl_student.heading('gpa', text='Điểm TB')
        self.tbl_student.heading('major', text='Chuyên ngành')
        # config columns
        self.tbl_student.column(0, stretch=tk.NO, width=100, anchor=tk.CENTER)
        self.tbl_student.column(1, stretch=tk.NO, width=150, anchor=tk.W)
        self.tbl_student.column(2, stretch=tk.NO, width=100, anchor=tk.CENTER)
        self.tbl_student.column(3, stretch=tk.NO, width=100, anchor=tk.CENTER)
        self.tbl_student.column(4, stretch=tk.NO, width=150, anchor=tk.W)
        self.tbl_student.column(5, stretch=tk.NO, width=100, anchor=tk.CENTER)
        self.tbl_student.column(6, stretch=tk.NO, width=150, anchor=tk.W)
        # add scrollbar
        scrollbar = ttk.Scrollbar(self.frame, orient=tk.VERTICAL, command=self.tbl_student.yview)
        scrollbar.grid(row=0, column=3, sticky=tk.NS)
        self.tbl_student['yscrollcommand'] = scrollbar.set
        # add buttons
        ttk.Button(self.frame, text='Load Students', command=self.load_student). \
            grid(row=1, column=0, ipady=4, ipadx=4)
        ttk.Button(self.frame, text='Edit GPA', command=self.edit_student). \
            grid(row=1, column=1, ipady=4, ipadx=4)
        ttk.Button(self.frame, text='Remove Items', command=self.remove_student). \
            grid(row=1, column=2, ipady=4, ipadx=4)

    def load_student(self):
        self.students.clear()
        self.students = self.controller.read_file(STUDENT_FILE_NAME)
        self.show_students()

    def show_students(self):
        clear_treeview(self.tbl_student)
        index = 1
        self.tbl_student.selection_clear()
        for student in self.students:
            if index % 2 == 0:
                tag = 'even'
            else:
                tag = 'odd'
            self.tbl_student.insert('', tk.END, values=student_to_tuple(student), tags=(tag,))
            index += 1

    def remove_student(self):
        item_selected = self.tbl_student.selection()
        if len(item_selected) > 0:
            title = 'Confirmation'
            message = 'Do you want to delete item(s) selected?'
            ans = askyesno(title, message)
            if ans:
                for item in item_selected:
                    index = int(item[1:], 16) - 1 # lấy vị trí hàng cần xóa - 1 có được vị trí phần tử trong danh sách
                    self.controller.remove(self.students, index)  # xóa phần tử trong danh sách sinh viên
                    self.tbl_student.delete(item)  # xóa phần tử trong bảng
                self.controller.write_file(STUDENT_FILE_NAME, self.students)  # update file
                showinfo(title='Infomation', message='Delete successfully!')
        else:
            showerror(title='Error', message='Please select a row to delete first!')

    def edit_student(self):
        item_selected = self.tbl_student.selection()
        if len(item_selected) > 0:
            item = item_selected[0]
            index = (int(item[1:], 16) - 1) % len(self.students)
            EditStudentView(self, self.students[index]).attributes('-topmost', True)

    def create_student(self, student: Student):
        self.students.append(student)
        self.show_students()

    def sort_by_name(self):
        self.controller.sort_by_name(self.students)
        # self.students.sort(key=lambda x: (x.full_name.first_name, x.full_name.last_name))
        self.show_students()

    def sort_by_birth_date(self):
        self.controller.sort_by_birth_date(self.students)
        self.show_students()

    def sort_by_gpa(self):
        self.controller.sort_by_gpa(self.students)
        self.show_students()

    def sort_by_gpa_and_name(self):
        self.controller.sort_by_name_gpa(self.students)
        self.show_students()

    def save(self):
        self.controller.write_file(STUDENT_FILE_NAME, students=self.students)
        showinfo('Successfully', 'Save students data to file successfully!')
