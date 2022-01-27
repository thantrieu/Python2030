import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


class LearnFrameLabel(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Learn FramLabel')
        self.geometry('360x220')
        self.resizable(False, False)
        self.configure(padx=8, pady=8)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.selected_size = tk.StringVar()
        self.selected_gender = tk.StringVar()
        self.create_frame_tshirt()
        self.create_frame_gender()
        self.create_submit_button()

    def create_submit_button(self):
        ttk.Button(text='Submit', command=self.show_result).\
            grid(row=1, column=0, columnspan=2, sticky=tk.EW, padx=4, pady=4)

    def create_frame_tshirt(self):
        frm = ttk.LabelFrame(text='What\'s your T-shirt size?')
        sizes = (
            ('Small', 'S'),
            ('Medium', 'M'),
            ('Large', 'L'),
            ('Extra Large', 'XL'),
            ('Extra Extra Large', 'XXL')
        )
        row = 0
        for size in sizes:
            ttk.Radiobutton(frm, text=size[0], value=size[1],
                            variable=self.selected_size) \
                .grid(row=row, column=0, sticky=tk.W, padx=4, pady=4)
            row += 1
        frm.grid(row=0, column=0, pady=4, padx=4, sticky=tk.NSEW)

    def create_frame_gender(self):
        frm = ttk.LabelFrame(text='What\'s your gender?')
        genders = (
            ('Male', 'M'),
            ('Female', 'F'),
            ('Lesbian', 'L'),
            ('Bisexual', 'B'),
            ('Transgender', 'T')
        )
        row = 0
        for gender in genders:
            ttk.Radiobutton(frm, text=gender[0],
                           value=gender[1], variable=self.selected_gender). \
                grid(row=row, column=0, padx=4, pady=4, sticky=tk.W)
            row += 1
        frm.grid(row=0, column=1, sticky=tk.NSEW, pady=4, padx=4)

    def show_result(self):
        msg = f'Gender: {self.selected_gender.get()}\nSize: {self.selected_size.get()}'
        showinfo(title='Result', message=msg)


if __name__ == '__main__':
    app = LearnFrameLabel()
    app.mainloop()
