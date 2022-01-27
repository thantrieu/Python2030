import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


class LearnRadiobutton(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Learn Radiobutton')
        self.geometry('300x220')
        self.resizable(False, False)
        self.selected_size = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        frm = ttk.Frame()
        sizes = (
            ('Small', 'S'),
            ('Medium', 'M'),
            ('Large', 'L'),
            ('Extra Large', 'XL'),
            ('Extra Extra Large', 'XXL')
        )
        ttk.Label(frm, text='What\'s your T-shirt size?'). \
            grid(row=0, column=0, sticky=tk.W, pady=5, padx=5)
        # add radio button
        index = 1
        for size in sizes:
            r = ttk.Radiobutton(frm, text=size[0],
                                value=size[1], variable=self.selected_size)
            r.grid(row=index, column=0, sticky=tk.W, pady=5, padx=5)
            index += 1
        frm.pack()

        # add button
        btn_submit = ttk.Button(text='Get Selected Size', command=self.show_selected_size)
        btn_submit.pack(fill='x', pady=5, padx=5)

    def show_selected_size(self):
        showinfo(title='Result', message=self.selected_size.get())


if __name__ == '__main__':
    app = LearnRadiobutton()
    app.mainloop()
