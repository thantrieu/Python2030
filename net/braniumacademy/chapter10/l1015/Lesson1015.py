# 1. Giới thiệu về Treeview
# 2. Thêm tiêu đề cho từng cột trong bảng
# 3. Cấu hình từng cột
# 4. Thêm dữ liệu vào bảng
# 5. Thêm thanh cuộn vào bảng
# 6. Xóa phần tử khỏi bảng
# 7. Yêu cầu bài tập: sửa dữ liệu 1 hàng được chọn

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, askyesno, showinfo

from student import Student


class LearnTreeview(tk.Tk):
    def __init__(self):
        super().__init__()
        self.table = None
        self.title('Learn Treeview')
        self.resizable(False, False)
        self.configure(pady=8, padx=8)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=4)
        self.rowconfigure(1, weight=1)
        self.create_widgets()

    def create_widgets(self):
        columns = ('id', 'last_name', 'first_name', 'gender', 'major', 'gpa')
        self.table = ttk.Treeview(columns=columns, show='headings', height=8)
        self.table.column(0, stretch=tk.NO, width=100, anchor=tk.CENTER)
        self.table.column(1, stretch=tk.NO, width=100, anchor=tk.CENTER)
        self.table.column(2, stretch=tk.NO, width=100, anchor=tk.CENTER)
        self.table.column(3, stretch=tk.NO, width=100, anchor=tk.CENTER)
        self.table.column(5, stretch=tk.NO, width=100, anchor=tk.CENTER)
        self.table.column(4, anchor=tk.CENTER)
        self.table.heading('id', text='Mã SV')
        self.table.heading('first_name', text='Tên')
        self.table.heading('last_name', text='Họ')
        self.table.heading('gender', text='Giới tính')
        self.table.heading('gpa', text='Điểm TB')
        self.table.heading('major', text='Chuyên ngành')
        self.table.insert()
        self.table.grid(row=0, column=0, sticky=tk.NSEW, pady=4, padx=4, columnspan=2)
        # add scrollbar
        scrollbar = ttk.Scrollbar(orient=tk.VERTICAL, command=self.table.yview)
        scrollbar.grid(row=0, column=2, sticky=tk.NS)
        self.table['yscrollcommand'] = scrollbar.set
        # add button
        ttk.Button(text='Load Data', command=self.load_data). \
            grid(row=1, column=0, ipady=4, ipadx=4)
        ttk.Button(text='Remove Items', command=self.remove_data). \
            grid(row=1, column=1, ipady=4, ipadx=4)

    def load_data(self):
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
            self.table.insert('', tk.END, values=student.totuple())

    def remove_data(self):
        item_selected = self.table.selection()
        if len(item_selected) > 0:
            title = 'Confirmation'
            message = 'Do you want to delete item(s) selected?'
            ans = askyesno(title, message)
            if ans:
                for item in item_selected:
                    self.table.delete(item)
                showinfo(title='Infomation', message='Delete successfully!')
        else:
            showerror(title='Error', message='Please select a row to delete first!')


if __name__ == '__main__':
    app = LearnTreeview()
    app.mainloop()
