import tkinter as tk
from tkinter import ttk
from tkinter import font


class LearnSlider(tk.Tk):
    def __init__(self):
        super().__init__()
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
        self.label = ttk.Label(text='Branium Academy', justify='center',
                               foreground='red', font=self.myfont)
        self.label.grid(row=0, column=0, columnspan=3, pady=8, padx=8)
        self.slider = ttk.Scale(from_=10, to=30, orient=tk.HORIZONTAL,
                                command=self.change_text_size,
                                variable=self.text_size)
        self.slider.grid(row=2, column=1, sticky=tk.EW, padx=16, pady=8)
        ttk.Label(text='10', foreground='red', font=('Arial', 14)).\
            grid(row=2, column=0, sticky=tk.E)
        ttk.Label(text='30', foreground='red', font=('Arial', 14)). \
            grid(row=2, column=2, sticky=tk.W)
        self.label_textsize = ttk.Label(text='Size: 10', foreground='Green', font=('Arial', 14))
        self.label_textsize.grid(row=1, column=1, padx=4, pady=4, sticky=tk.S)

    def change_text_size(self, event):
        size = int(self.text_size.get())
        self.label_textsize.configure(text=f'Size: {size}')
        self.myfont.configure(size=size)


if __name__ == '__main__':
    app = LearnSlider()
    app.mainloop()
