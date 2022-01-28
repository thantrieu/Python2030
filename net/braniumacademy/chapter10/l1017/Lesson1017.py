import tkinter as tk
from tkinter import ttk
from tkinter import font


class LearnSlider(tk.Tk):
    def __init__(self):
        super(LearnSlider, self).__init__()
        self.title('Learn Slider')
        self.geometry('360x200')
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=8)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=3)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.text_size = tk.DoubleVar()
        self.myfont = font.Font(family='Arial', size=10)
        self.create_widgets()

    def create_widgets(self):
        self.lable = ttk.Label(text='Branium Academy', foreground='red',
                               justify='center', font=self.myfont)
        self.lable_size = ttk.Label(text='Size: 10', foreground='green', font=('Arial', 14))
        self.lable_size.grid(row=1, column=1, padx=4, pady=4, sticky=tk.S)
        # min and max label
        ttk.Label(text='10', foreground='red', font=('Arial', 14)). \
            grid(row=2, column=0, sticky=tk.E)
        ttk.Label(text='30', foreground='red', font=('Arial', 14)). \
            grid(row=2, column=2, sticky=tk.W)
        self.lable.grid(row=0, column=0, columnspan=3, padx=8, pady=8)
        # add slider
        self.slider = ttk.Scale(variable=self.text_size, from_=10, to=30,
                                orient=tk.HORIZONTAL, command=self.change_text_size)
        self.slider.grid(row=2, column=1, sticky=tk.EW, pady=4, padx=16)

    def change_text_size(self, event):
        size = int(self.text_size.get())
        self.lable_size.configure(text=f'Size: {size}')
        self.myfont.configure(size=size)


if __name__ == '__main__':
    app = LearnSlider()
    app.mainloop()
