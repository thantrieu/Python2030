import tkinter as tk
from tkinter import ttk
from tkinter import colorchooser


class LearnColorChooser(tk.Tk):
    def __init__(self):
        super(LearnColorChooser, self).__init__()
        self.title('Learn Color Chooser')
        self.geometry('300x150')
        self.resizable(False, False)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        ttk.Button(text='Select Background Color',
                   command=lambda: self.change_bg_color()).\
            grid(row=0, column=0, ipadx=8, ipady=4)

    def change_bg_color(self):
        colors = colorchooser.askcolor()
        color = colors[1]
        if color is not None:
            self.configure(background=color)


if __name__ == '__main__':
    obj = LearnColorChooser()
    obj.mainloop()
