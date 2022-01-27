# 1. Giới thiệu về Text widget
# 2. Đọc và chèn dữ liệu vào Text widget
# 3. Ví dụ minh họa

import tkinter
from tkinter import ttk
from tkinter.messagebox import showinfo, showwarning


class LearnText(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title('Learn Text Widget')
        self.configure(padx=16, pady=8)
        self.create_widgets()

    def create_widgets(self):
        self.txt_comment = tkinter.Text(height=8, width=40, padx=8)
        self.txt_comment.grid(row=0, column=0, sticky=tkinter.NSEW)
        btn_submit = ttk.Button(text='Submit', command=self.submit, padding=4)
        btn_submit.grid(column=0, row=1)

    def submit(self):
        data = self.txt_comment.get('1.0', 'end').strip()
        if len(data) == 0:
            showwarning(title='Attention', message='Your comment cannot be blank!')
        else:
            showinfo(title='Your comment', message=data)


if __name__ == '__main__':
    app = LearnText()
    app.mainloop()
