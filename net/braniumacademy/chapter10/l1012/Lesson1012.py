# 1. Hộp thoại Yes/No
# 2. Hộp thoại Yes/No/Cancel
# 3. Hộp thoại Ok/Cancel
# 4. Hộp thoại Retry/Cancel
# 5. Hộp thoại askquestion

import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as msgbox


class LearnConfirmDialog(tk.Tk):
    def __init__(self):
        super(LearnConfirmDialog, self).__init__()
        self.title('Learn Confirm Dialog')
        self.geometry('300x200')
        self.configure(pady=16, padx=16)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.create_widgets()

    def create_widgets(self):
        ttk.Button(text='Quit', command=self.btn_quit_clicked). \
            grid(row=0, column=0, padx=4, pady=4)
        ttk.Button(text='Delete All', command=self.btn_delete_clicked). \
            grid(row=1, column=0, padx=4, pady=4)
        ttk.Button(text='Connect Database', command=self.btn_retry_clicked). \
            grid(row=2, column=0, padx=4, pady=4)

    def btn_quit_clicked(self):
        title = 'Confirmation'
        message = 'Do you want to quit?'
        ans = msgbox.askyesnocancel(title=title, message=message)
        if ans:
            self.destroy()

    def btn_retry_clicked(self):
        title = 'Connection Issue'
        message = 'The server is unreachable. Do you want to retry?'
        ans = msgbox.askretrycancel(title, message)
        if ans:
            # reconnect to db
            message = 'Attempt reconnect to the database...'
            msgbox.showinfo(title='Infomation', message=message)

    def btn_delete_clicked(self):
        title = 'Attention'
        message = 'All data will be permanently deleted.'
        ans = msgbox.askokcancel(title, message)
        if ans:
            # delete data, show result after delete
            msg = 'All data has been deleted successfully.'
            msgbox.showinfo(title, message=msg)


if __name__ == '__main__':
    app = LearnConfirmDialog()
    app.mainloop()
