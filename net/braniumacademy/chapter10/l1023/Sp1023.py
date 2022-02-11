import tkinter as tk
from tkinter import ttk
import tkinter.filedialog as fd


class LearnColorChooser(tk.Tk):
    def __init__(self):
        super(LearnColorChooser, self).__init__()
        self.title('Learn File Dialog')
        self.geometry('300x200')
        self.resizable(False, False)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        ttk.Button(text='Select File Name',
                   command=lambda: self.change_bg_color()). \
            grid(row=0, column=0, ipady=4, ipadx=8)

    def change_bg_color(self):
        path = r'C:\Users\trieu\PycharmProjects\LeanPython\net\braniumacademy\chapter10'
        # file_name = fd.askopenfilenames(initialdir=path, defaultextension='*.*', filetypes=[('All files', '*.*')]) # trả về tên file được chọn
        # print(file_name)
        # with open(file_name[0]) as reader:
        #     print(reader.read())
        f = fd.askopenfile(initialdir=path)
        # fd.asksaveasfilename()
        if f is not None:
            print(f.read())

if __name__ == '__main__':
    obj = LearnColorChooser()
    obj.mainloop()
