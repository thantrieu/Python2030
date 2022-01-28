# 1. Giới thiệu về Notebook
# 2. Ví dụ minh họa

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, askyesno, showinfo
from student import Student


class LearnNotebook(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Learn Notebook')
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.configure(padx=8, pady=8)
        self.create_notebook()
        self.create_student_widgets()
        self.create_subject_widgets()

    def create_notebook(self):
        notebook = ttk.Notebook()
        notebook.grid(row=0, column=0, sticky=tk.NSEW)
        self.frame1 = ttk.Frame(notebook)
        self.frame1.rowconfigure(0, weight=4)
        self.frame1.rowconfigure(1, weight=1)
        self.frame1.columnconfigure(0, weight=1)
        self.frame1.columnconfigure(1, weight=1)
        self.frame1.grid(row=0, column=0)
        # add second frame
        self.frame2 = ttk.Frame(notebook)
        self.frame2.rowconfigure(0, weight=4)
        self.frame2.rowconfigure(1, weight=1)
        self.frame2.columnconfigure(0, weight=1)
        self.frame2.columnconfigure(1, weight=1)
        self.frame2.grid(row=0, column=0)
        notebook.add(self.frame1, text='Student Managerment')
        notebook.add(self.frame2, text='Subject Managerment')

    def create_student_widgets(self):
        columns = ('id', 'last_name', 'first_name', 'gender', 'major', 'gpa')
        self.tbl_student = ttk.Treeview(self.frame1, columns=columns, show='headings', height=8)
        self.tbl_student.grid(row=0, column=0, columnspan=2, sticky=tk.NSEW, pady=4, padx=4)
        # show heading
        self.tbl_student.heading('id', text='Mã SV')
        self.tbl_student.heading('first_name', text='Tên')
        self.tbl_student.heading('last_name', text='Họ')
        self.tbl_student.heading('gender', text='Giới tính')
        self.tbl_student.heading('gpa', text='Điểm TB')
        self.tbl_student.heading('major', text='Chuyên ngành')
        # config columns
        self.tbl_student.column(0, stretch=tk.NO, width=100, anchor=tk.CENTER)
        self.tbl_student.column(1, stretch=tk.NO, width=100, anchor=tk.CENTER)
        self.tbl_student.column(2, stretch=tk.NO, width=100, anchor=tk.CENTER)
        self.tbl_student.column(3, stretch=tk.NO, width=100, anchor=tk.CENTER)
        self.tbl_student.column(5, stretch=tk.NO, width=100, anchor=tk.CENTER)
        self.tbl_student.column(4, stretch=tk.NO, width=160, anchor=tk.CENTER)
        # add scrollbar
        scrollbar = ttk.Scrollbar(self.frame1, orient=tk.VERTICAL, command=self.tbl_student.yview)
        scrollbar.grid(row=0, column=2, sticky=tk.NS)
        self.tbl_student['yscrollcommand'] = scrollbar.set
        # add buttons
        ttk.Button(self.frame1, text='Load Students', command=self.load_student). \
            grid(row=1, column=0, ipady=4, ipadx=4)
        ttk.Button(self.frame1, text='Remove Items', command=self.remove_student). \
            grid(row=1, column=1, ipady=4, ipadx=4)

    def load_student(self):
        file_name = 'input.txt'
        students = []
        with open(file_name, 'r', encoding='UTF-8') as reader:
            student_id = reader.readline().strip()
            while True:
                name = reader.readline().strip()
                gender = reader.readline().strip()
                major = reader.readline().strip()
                gpa = float(reader.readline())
                students.append(Student(student_id, name, gender, major, gpa))
                student_id = reader.readline().strip()
                if student_id == '':
                    break
        self.show_students(students)

    def show_students(self, mstudents):
        for student in mstudents:
            self.tbl_student.insert('', tk.END, values=student.totuple())

    def remove_student(self):
        item_selected = self.tbl_student.selection()
        if len(item_selected) > 0:
            title = 'Confirmation'
            message = 'Do you want to delete item(s) selected?'
            ans = askyesno(title, message)
            if ans:
                for item in item_selected:
                    self.tbl_student.delete(item)
                showinfo(title='Infomation', message='Delete successfully!')
        else:
            showerror(title='Error', message='Please select a row to delete first!')

    def create_subject_widgets(self):
        columns = ('id', 'name', 'lesson', 'credit')
        self.tbl_subject = ttk.Treeview(self.frame2, columns=columns, show='headings', height=8)
        self.tbl_subject.grid(row=0, column=0, columnspan=2, sticky=tk.NSEW, pady=4, padx=4)
        # show heading
        self.tbl_subject.heading('id', text='Mã môn học')
        self.tbl_subject.heading('name', text='Tên môn học')
        self.tbl_subject.heading('lesson', text='Số tiết')
        self.tbl_subject.heading('credit', text='Số tín chỉ')
        # config columns
        self.tbl_subject.column(0, stretch=tk.NO, width=165, anchor=tk.CENTER)
        self.tbl_subject.column(1, stretch=tk.NO, width=165, anchor=tk.CENTER)
        self.tbl_subject.column(2, stretch=tk.NO, width=165, anchor=tk.CENTER)
        self.tbl_subject.column(3, stretch=tk.NO, width=165, anchor=tk.CENTER)
        # add scrollbar
        scrollbar = ttk.Scrollbar(self.frame2, orient=tk.VERTICAL, command=self.tbl_subject.yview)
        scrollbar.grid(row=0, column=2, sticky=tk.NS)
        self.tbl_subject['yscrollcommand'] = scrollbar.set
        # add buttons
        ttk.Button(self.frame2, text='Load Subject', command=self.load_subject). \
            grid(row=1, column=0, ipady=4, ipadx=4)
        ttk.Button(self.frame2, text='Remove Items', command=self.remove_subject). \
            grid(row=1, column=1, ipady=4, ipadx=4)

    def load_subject(self):
        pass

    def remove_subject(self):
        pass


if __name__ == '__main__':
    app = LearnNotebook()
    app.mainloop()
