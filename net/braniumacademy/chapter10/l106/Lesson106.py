# 1. Giới thiệu Frame
# 2. Ví dụ minh họa

import tkinter as tk
from tkinter import ttk


class LearnFrame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Learn Frame Widget')
        self.geometry('400x150')
        self.resizable(False, False)
        self.columnconfigure(0, weight=4)
        self.columnconfigure(1, weight=1)
        self.create_iput_frame()
        self.create_button_frame()

    def create_iput_frame(self):
        frm = ttk.Frame()
        frm.columnconfigure(0, weight=1)
        frm.columnconfigure(1, weight=3)
        # find what
        ttk.Label(frm, text='Find what: ').grid(row=0, column=0, sticky=tk.W)
        key = ttk.Entry(frm, width=30)
        key.focus()
        key.grid(row=0, column=1, sticky=tk.EW)
        # replace with
        ttk.Label(frm, text='Replace with: ').grid(row=1, column=0, sticky=tk.W)
        rep = ttk.Entry(frm, width=30)
        rep.grid(row=1, column=1, sticky=tk.EW)
        frm.grid(row=0, column=0)
        # checkbox
        wrap_around = tk.IntVar()
        match_case = tk.IntVar()
        match_case_check = ttk.Checkbutton(frm, text='Match case',
                                           variable=match_case,
                                           command=lambda: print(match_case.get()))
        match_case_check.grid(row=2, column=0, sticky=tk.W)
        wrap_around_check = ttk.Checkbutton(frm, text='Wrap around',
                                            variable=wrap_around,
                                            command=lambda: print(wrap_around.get()))
        wrap_around_check.grid(row=3, column=0, sticky=tk.W)
        # add padding
        for e in frm.winfo_children():
            e.grid(pady=5)
        frm.grid(row=0, column=0)

    def create_button_frame(self):
        frm = ttk.Frame()
        ttk.Button(frm, text='Find Next').grid(row=0, column=0)
        ttk.Button(frm, text='Replace').grid(row=1, column=0)
        ttk.Button(frm, text='Replace All').grid(row=2, column=0)
        ttk.Button(frm, text='Cancel').grid(row=3, column=0)
        # add padding
        for e in frm.winfo_children():
            e.grid(pady=3)

        frm.grid(row=0, column=1)


if __name__ == '__main__':
    app = LearnFrame()
    app.mainloop()
