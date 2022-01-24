import tkinter as tk
from functools import partial
from tkinter import ttk
from tkinter.messagebox import showinfo, showwarning, askyesno


class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.ico_like = tk.PhotoImage(file='like.png')
        self.ico_dislike = tk.PhotoImage(file='dislike.png')
        self.ico_quit = tk.PhotoImage(file='close.png')
        self.geometry('300x200')
        self.rowconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        # self.rowconfigure(1, weight=1)
        # self.rowconfigure(2, weight=1)
        # self.columnconfigure(0, weight=1)
        # self.columnconfigure(1, weight=1)
        # self.grid(baseWidth=1, baseHeight=1, widthInc=1, heightInc=1)
        self.title('Learn Button')
        self.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        frm = ttk.Frame(padding=8)
        frm.grid(row=0, column=0, sticky='')
        frm.grid_rowconfigure(0, weight=1)
        frm.grid_columnconfigure(0, weight=1)
        btn_like = ttk.Button(frm, text='Like', image=self.ico_like,
                              compound=tk.LEFT,
                              command=partial(showinfo, title='Infomation',
                                              message='Like button clicked!'))
        # style = ttk.Style()
        # style.configure('TButton', background='green', width=50)
        # style.map('TButton', background=[('active', 'red'), ('hover', 'gray')])
        btn_like.grid(row=0, column=0, padx=4, pady=4)
        btn_dislike = ttk.Button(frm, text='Dislike', image=self.ico_dislike,
                                 compound=tk.LEFT,
                                 command=partial(showwarning, title='Infomation',
                                                 message='Dislike button clicked!'),
                                 )
        btn_dislike.grid(row=1, column=0, pady=4, padx=4)
        btn_close = ttk.Button(frm, text='Quit', image=self.ico_quit,
                               command=self.confirm, compound=tk.LEFT)
        btn_close.grid(row=2, column=0, columnspan=2, pady=4, padx=4)

    def confirm(self):
        answer = askyesno(title='Confirm your action',
                          message='Do you want to quit?')
        if answer:
            self.destroy()


if __name__ == '__main__':
    app = MyApp()
    app.mainloop()
