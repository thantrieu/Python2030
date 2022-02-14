import tkinter as tk
from tkinter import ttk


class SearchStudent(tk.Tk):
    def __init__(self, master, pos: int = 0):
        super(SearchStudent, self).__init__()
        self.title('Search Student')
        self.radio_selected = tk.IntVar(value=pos)
        self.create_widgets()

    def create_widgets(self):
        frm = ttk.LabelFrame(self, text='Search By')
        frm.grid(row=0, column=0, pady=4, padx=4, sticky=tk.NSEW)
        radio1 = ttk.Radiobutton(frm, text='Search By Name',
                                 variable=self.radio_selected, value=0)
        radio1.grid(row=0, column=0, sticky=tk.W, padx=8)
        # if self.radio_selected.get() == 0:
        #     radio1.select()
        ttk.Radiobutton(frm, text='Search By GPA',
                        variable=self.radio_selected, value=1). \
            grid(row=1, column=0, sticky=tk.W, padx=8)
        ttk.Radiobutton(frm, text='Search By Day',
                        variable=self.radio_selected, value=2). \
            grid(row=2, column=0, sticky=tk.W, padx=8)
        ttk.Radiobutton(frm, text='Search By Month',
                        variable=self.radio_selected, value=3). \
            grid(row=0, column=1, sticky=tk.W, padx=8)
        ttk.Radiobutton(frm, text='Search By Year',
                        variable=self.radio_selected, value=4). \
            grid(row=1, column=1, sticky=tk.W, padx=8)
        self.entry_value = ttk.Entry()
        ttk.Label(text='Key: ')
        ttk.Button(text='Cancel', command=self.destroy)
        ttk.Button(text='Search', command=lambda: self.search())


def search(self):
    pass
