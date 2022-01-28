import time
from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import showinfo


class LearnProgressbar(tk.Tk):
    def __init__(self):
        super(LearnProgressbar, self).__init__()
        self.progressbar = None
        self.value_label = None
        self.geometry('300x120')
        self.title('Learn Progressbar')
        self.create_widgets()

    def create_widgets(self):
        # progressbar
        self.progressbar = ttk.Progressbar(orient='horizontal', mode='determinate', length=280)
        # self.progressbar.start(500)
        # self.progressbar.step(200)
        # place the progressbar
        self.progressbar.grid(column=0, row=0, columnspan=2, padx=10, pady=20)
        # label
        self.value_label = ttk.Label(text=self.update_progress_label())
        self.value_label.grid(column=0, row=1, columnspan=2)
        # start button
        start_button = ttk.Button(text='Progress', command=self.progress)
        start_button.grid(column=0, row=2, padx=10, pady=10, sticky=tk.E)
        stop_button = ttk.Button(text='Stop', command=self.stop)
        stop_button.grid(column=1, row=2, padx=10, pady=10, sticky=tk.W)

    def update_progress_label(self):
        return f"Current Progress: {self.progressbar['value']}%"

    def progress(self):
        for i in range(10):
            self.update_idletasks()
            self.progressbar['value'] += 10
            self.value_label['text'] = self.update_progress_label()
            time.sleep(1)
        showinfo('Infomation', message='The progress completed!')

    def stop(self):
        self.progressbar.stop()
        self.value_label['text'] = self.update_progress_label()


if __name__ == '__main__':
    obj = LearnProgressbar()
    obj.mainloop()
