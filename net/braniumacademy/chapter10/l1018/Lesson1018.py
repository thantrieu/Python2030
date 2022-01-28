import time
from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import showinfo


class LearnProgressbar(tk.Tk):
    def __init__(self):
        super(LearnProgressbar, self).__init__()
        self.title('Learn Progressbar')
        self.geometry('300x120')
        self.create_widgets()

    def create_widgets(self):
        self.progressbar = ttk.Progressbar(mode='determinate', length=280)
        self.progressbar.grid(row=0, column=0, columnspan=2, padx=10, pady=16)
        # add label current progress
        self.label_progress = ttk.Label(text=self.update_progress_label())
        self.label_progress.grid(row=1, column=0, columnspan=2)
        # add button
        ttk.Button(text='Start', command=self.start). \
            grid(row=2, column=0, pady=4, padx=4, sticky=tk.E)
        ttk.Button(text='Stop', command=self.stop). \
            grid(row=2, column=1, pady=4, padx=4, sticky=tk.W)

    def start(self):
        # self.progressbar.start(100)
        # self.progressbar.step(50)
        for i in range(10):
            if self.progressbar['value'] < 100:
                self.update_idletasks()
                self.progressbar['value'] += 10
                self.label_progress.configure(text=self.update_progress_label())
                time.sleep(0.5)
        showinfo('Infomation', "The progress completed!")

    def stop(self):
        self.progressbar.stop()
        self.label_progress.configure(text=self.update_progress_label())

    def update_progress_label(self):
        return f'Current progress: {self.progressbar["value"]}%'


if __name__ == '__main__':
    obj = LearnProgressbar()
    obj.mainloop()
