# 1. Giới thiệu về phần tử button widget
# 2. Giới thiệu về command callback
# 3. Trạng thái của một button
# 4. Ví dụ minh họa

import tkinter
from tkinter import ttk
from functools import partial
from tkinter.messagebox import showinfo, showwarning, askyesno


class LearnButton(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.ico_like = tkinter.PhotoImage(file='like.png')
        self.ico_dislike = tkinter.PhotoImage(file='dislike.png')
        self.ico_quit = tkinter.PhotoImage(file='close.png')
        self.title('Learn Button')
        self.geometry('300x200')
        self.resizable(False, False)
        self.rowconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)  # Cấu hình cho phép đưa phần tử ra giữa ô theo chiều ngang
        self.grid_columnconfigure(0, weight=1)  # cho phép đưa phần tử ra giữa ô theo chiều dọc
        self.create_widgets()

    def create_widgets(self):
        frm = ttk.Frame(padding=8)
        frm.grid(row=0, column=0, sticky='')
        frm.grid_rowconfigure(0, weight=1)
        frm.grid_columnconfigure(0, weight=1)
        btn_like = ttk.Button(frm, text='Like', image=self.ico_like,
                              compound=tkinter.LEFT,
                              command=partial(
                                  showinfo,
                                  title='Infomation',
                                  message='Like button clicked!'
                              ))
        btn_like.grid(row=0, column=0)
        btn_dislike = ttk.Button(frm, text='Dislike', image=self.ico_dislike,
                                 compound=tkinter.LEFT,
                                 command=partial(
                                     showwarning,
                                     title='Warning',
                                     message='Dislike button clicked!'
                                 )
                                 )
        btn_dislike.grid(row=1, column=0)
        btn_quit = ttk.Button(frm, text='Quit', image=self.ico_quit,
                              compound=tkinter.LEFT,
                              command=self.btn_quit_clicked)
        btn_quit.grid(row=2, column=0)

    def btn_quit_clicked(self):
        answer = askyesno(title='Confirmation', message='Do you want to quit?')
        if answer:
            self.destroy()  # thoát chương trình


if __name__ == '__main__':
    app = LearnButton()
    app.mainloop()
