import tkinter as tk
from tkinter import ttk
from tkinter import font


class LearnSpinbox(tk.Tk):
    def __init__(self):
        super(LearnSpinbox, self).__init__()
        self.current_value = tk.StringVar(value='10')
        self.spinbox = None
        self.lable_size = None
        self.label_message = None
        self.title('Learn Spinbox')
        self.geometry('360x200')
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=3)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.myfont = font.Font(family='Arial', size=10)
        self.create_widgets()

    def create_widgets(self):
        self.label_message = ttk.Label(text='Branium Academy', foreground='red',
                                       justify='center', font=self.myfont)
        self.lable_size = ttk.Label(text='Size: 10', foreground='green', font=('Arial', 14))
        self.lable_size.grid(row=1, column=0, columnspan=3, padx=4, pady=4, sticky=tk.S)
        # hint label
        ttk.Label(text='Choose text size:', foreground='red', font=('Arial', 12)). \
            grid(row=2, column=0, sticky=tk.E)
        self.label_message.grid(row=0, column=0, columnspan=3, padx=8, pady=8)
        # add spinbox
        self.spinbox = ttk.Spinbox(from_=10, to=30,
                                   # values=['10', '15', '20', '25', '30'],
                                   textvariable=self.current_value,
                                   wrap=True,
                                   command=self.change_text_size)
        self.spinbox.grid(row=2, column=1, sticky=tk.EW, pady=4, padx=16)

    def change_text_size(self, *args):
        size = int(self.current_value.get())
        self.lable_size.configure(text=f'Size: {size}')
        self.myfont.configure(size=size)


if __name__ == '__main__':
    app = LearnSpinbox()
    app.mainloop()
