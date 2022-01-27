import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


class LearnRadiobutton(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Learn Radiobutton')
        self.geometry('360x220')
        self.resizable(False, False)
        self.selected_size = tk.StringVar()
        self.gender = tk.StringVar()
        self.configure(padx=8, pady=8)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.create_frame_tshirt()
        self.create_frame_gender()

    def create_frame_gender(self):
        """Create frame contains genders like male, female, LGBT"""
        frm = ttk.LabelFrame(text='What\'s your gender?')
        genders = (
            ('Male', 'M'),
            ('Female', 'F'),
            ('Lesbian', 'L'),
            ('Bisexual', 'B'),
            ('Transgender', 'T')
        )
        pos = 0
        for gender in genders:
            ttk.Radiobutton(frm, text=gender[0],
                            value=gender[1], variable=self.gender) \
                .grid(row=pos, column=0, pady=4, padx=4, sticky=tk.W)
            pos += 1
        frm.grid(row=0, column=1, pady=4, padx=4, sticky=tk.NSEW)

    def create_frame_tshirt(self):
        """Create frame with radio buttons describe tshirt size"""
        frm = ttk.LabelFrame(text='What\'s your T-shirt size?')
        sizes = (
            ('Small', 'S'),
            ('Medium', 'M'),
            ('Large', 'L'),
            ('Extra Large', 'XL'),
            ('Extra Extra Large', 'XXL')
        )
        # add radio button
        index = 1
        for size in sizes:
            r = ttk.Radiobutton(frm, text=size[0],
                                value=size[1], variable=self.selected_size)
            r.grid(row=index, column=0, sticky=tk.W, pady=4, padx=4)
            index += 1
        frm.grid(row=0, column=0)

        # add button
        btn_submit = ttk.Button(text='Submit', command=self.show_selected_size)
        btn_submit.grid(row=1, column=0, columnspan=2, pady=4, padx=4, sticky=tk.NSEW)

    def show_selected_size(self):
        """Show result via selected radio buttons"""
        msg = f'Gender: {self.gender.get()}\nSize: {self.selected_size.get()}'
        showinfo(title='Result', message=msg)


if __name__ == '__main__':
    app = LearnRadiobutton()
    app.mainloop()
