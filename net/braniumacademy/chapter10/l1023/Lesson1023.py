import tkinter as tk
from tkinter import ttk
import tkinter.filedialog as fd


class LearnFileDialog(tk.Tk):
    def __init__(self):
        super(LearnFileDialog, self).__init__()
        self.title('Learn File Dialog')
        self.geometry('300x200')
        self.resizable(False, False)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        ttk.Button(text='Select File Name',
                   command=lambda: self.select_file()). \
            grid(row=0, column=0, ipady=4, ipadx=8)

    def select_file(self):
        # thay đường dẫn thành đường dẫn trên máy của bạn
        default_path = r'C:\Users\trieu\PycharmProjects\LeanPython\net\braniumacademy\chapter10'
        file_types = [('All files', '*.*'), ('Python file', '*.py'), ('Image files', '*.png')]
        # selected_files = fd.askopenfilenames(initialdir=default_path,
        #                                    filetypes=file_types)
        # print(selected_files)
        # with open(selected_file) as reader:
        #     print(reader.read())
        # thay đường dẫn thành đường dẫn trong máy của bạn
        reader = fd.askopenfile(filetypes=file_types,
                                initialdir=default_path)
        if reader is not None:
            print(reader.read())


if __name__ == '__main__':
    obj = LearnFileDialog()
    obj.mainloop()
