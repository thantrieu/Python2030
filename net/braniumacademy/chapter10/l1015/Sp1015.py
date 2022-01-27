from student import Student
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, askyesno, askokcancel, showerror


class LearnTreeview(tk.Tk):
    def __init__(self):
        super().__init__()
        self.table = None
        self.title('Learn Treeview')
        self.resizable(False, False)
        self.configure(padx=16, pady=16)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=4)
        self.rowconfigure(1, weight=1)
        self.selected_day = tk.StringVar()
        self.selected_month = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        columns = ('id', 'first_name', 'last_name', 'gender', 'major', 'gpa')
        self.table = ttk.Treeview(columns=columns, show='headings', height=8)
        self.table.heading('id', text='Mã SV')
        self.table.heading('first_name', text='Tên')
        self.table.heading('last_name', text='Họ')
        self.table.heading('gender', text='Giới tính')
        self.table.heading('major', text='Chuyên ngành')
        self.table.heading('gpa', text='Điểm TB')
        self.table.column(0, stretch=tk.NO, width=100)
        self.table.column(1, stretch=tk.NO, width=100)
        self.table.column(2, stretch=tk.NO, width=100)
        self.table.column(3, stretch=tk.NO, width=100)
        self.table.column(5, stretch=tk.NO, width=100)
        self.table.grid(row=0, column=0, sticky=tk.NSEW, pady=4, padx=4, columnspan=2)
        # self.table.bind('<<TreeviewSelect>>', self.item_selected)
        # add scrollbar
        scrollbar = ttk.Scrollbar(orient=tk.VERTICAL, command=self.table.yview)
        scrollbar.grid(row=0, column=2, sticky=tk.NS)
        self.table['yscrollcommand'] = scrollbar.set
        # add load data button
        ttk.Button(text='Load Data', command=self.load_data) \
            .grid(row=1, column=0, ipadx=4, ipady=4)
        # add remove button
        ttk.Button(text='Remove rows', command=self.remove_data) \
            .grid(row=1, column=1, ipadx=4, ipady=4)

    def remove_data(self):
        # for item in self.table.selection():
        #     print(self.table.item(item)['values'])
        title = 'Confirmation'
        message = 'Do you want to delete item(s) selected?'
        item_selected = self.table.selection()
        if len(item_selected) > 0:
            ans = askokcancel(title=title, message=message)
            if ans:
                for item in item_selected:
                    if item is not None:
                        self.table.delete(item)
                showinfo(title='Infomation', message='Delete successfully!')
        else:
            showerror(title='Error', message='Please select a row to delete first!')

    def load_data(self):
        file_name = 'input.txt'
        mstudents = []
        with open(file_name, encoding='UTF-8') as reader:
            student_id = reader.readline().strip()
            while True:
                name = reader.readline().strip()
                gender = reader.readline().strip()
                major = reader.readline().strip()
                gpa = float(reader.readline())
                mstudents.append(Student(student_id, name, gender, major, gpa))
                student_id = reader.readline().strip()
                if student_id == '':
                    break
        self.show_students(mstudents)

    def show_students(self, mstudents):
        for student in mstudents:
            self.table.insert('', tk.END, values=student.totuple())


if __name__ == '__main__':
    app = LearnTreeview()
    app.mainloop()
