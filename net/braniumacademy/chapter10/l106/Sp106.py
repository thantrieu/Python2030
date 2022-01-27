import tkinter
from tkinter import ttk


class LearnFrame(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title('Learn Frame Widget')
        # self.configure(padx=16, pady=16)
        self.geometry('400x150')
        self.resizable(False, False)
        # self.attributes('-toolwindow', True)
        self.columnconfigure(0, weight=4)
        self.columnconfigure(1, weight=1)
        self.create_input_frame()
        self.create_button_frame()

    def create_input_frame(self):
        frm = ttk.Frame()
        frm.columnconfigure(0, weight=1)
        frm.columnconfigure(1, weight=3)
        # find what
        ttk.Label(frm, text='Find what: ').grid(row=0, column=0, sticky=tkinter.W)
        key = ttk.Entry(frm, width=30)
        key.focus()
        key.grid(row=0, column=1, sticky=tkinter.EW)

        # replace with
        ttk.Label(frm, text='Replace with: ').grid(row=1, column=0, sticky=tkinter.W)
        replacement = ttk.Entry(frm, width=30)
        replacement.grid(row=1, column=1, sticky=tkinter.EW)

        # checkbox
        wrap_around = tkinter.IntVar()
        match_case = tkinter.IntVar()
        match_case_check = ttk.Checkbutton(frm, text='Match case',
                                           variable=match_case,
                                           command=lambda: print(match_case.get()))
        wrap_around_check = ttk.Checkbutton(frm, text='Wrap around',
                                            variable=wrap_around,
                                            command=lambda: print(wrap_around.get()))
        wrap_around_check.grid(column=0, row=3, sticky=tkinter.W)
        match_case_check.grid(column=0, row=2, sticky=tkinter.W)

        # add padding y
        for e in frm.winfo_children():
            e.grid(pady=5, padx=2)
        frm.grid(row=0, column=0)

    def create_button_frame(self):
        frm = ttk.Frame()
        ttk.Button(frm, text='Find Next').grid(column=0, row=0)
        ttk.Button(frm, text='Replace').grid(column=0, row=1)
        ttk.Button(frm, text='Replace All').grid(column=0, row=2)
        ttk.Button(frm, text='Cancel').grid(column=0, row=3)
        # add padding
        for e in frm.winfo_children():
            e.grid(padx=2, pady=3)
        frm.grid(row=0, column=1)


if __name__ == '__main__':
    app = LearnFrame()
    app.mainloop()
