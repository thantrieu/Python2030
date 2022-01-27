import tkinter
from tkinter import ttk
from tkinter.messagebox import showinfo


class LearnText(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title('Learn Text Widget')
        # self.geometry('320x180')
        self.configure(pady=8, padx=16)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.create_widgets()

    def create_widgets(self):
        self.txt_comment = tkinter.Text(height=8, width=40, padx=8)
        self.txt_comment.grid(row=0, column=0, sticky=tkinter.NSEW)
        # self.txt_comment.place(anchor=tkinter.CENTER, relx=0.5, rely=0.5)
        self.txt_comment.insert('0.0', 'Nhập comment của bạn vào đây')
        btn_submit = ttk.Button(text='Submit', command=self.submit, padding=4)
        btn_submit.grid(row=1, column=0)

    def submit(self):
        showinfo(title='Your Comment', message=self.txt_comment.get('0.0', 'end'))


if __name__ == '__main__':
    app = LearnText()
    app.mainloop()
