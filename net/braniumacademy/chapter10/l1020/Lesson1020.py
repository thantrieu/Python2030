import tkinter as tk
from tkinter import Menu


class LearnMenu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Learn Menu')
        self.geometry('300x200')
        self.menubar = Menu()
        self.configure(menu=self.menubar)
        self.create_widgets()
        self.binding_events()

    def create_widgets(self):
        file_menu = Menu(self.menubar, tearoff=False)
        file_menu.add_command(label='Open', underline=0)
        file_menu.add_command(label='Find', underline=0)
        file_menu.add_command(label='Close', underline=0)
        # add separator and sub menu
        file_menu.add_separator()
        sub_menu = Menu(file_menu, tearoff=False)
        sub_menu.add_command(label='Theme')
        sub_menu.add_command(label='Font')
        sub_menu.add_command(label='Background Color')
        sub_menu.add_command(label='Window Size')
        file_menu.add_cascade(label='Preferences', menu=sub_menu)
        file_menu.add_separator()
        file_menu.add_command(label='Exit', underline=0, command=self.destroy)
        # add to menu bar
        self.menubar.add_cascade(label='File', menu=file_menu, underline=0)
        # add help menu
        help_menu = Menu(self.menubar, tearoff=False)
        help_menu.add_command(label='Welcome')
        help_menu.add_command(label='About Us')
        help_menu.add_command(label='Other')
        self.menubar.add_cascade(label='Help', menu=help_menu, underline=0)
        # add color menu
        color_menu = Menu(self.menubar, tearoff=False)
        self.selected_color = tk.IntVar()
        color_menu.add_radiobutton(label='Red', underline=0, value=1,
                                   variable=self.selected_color,
                                   command=lambda: self.change_background_color('red'),
                                   accelerator='Shift+R')
        color_menu.add_radiobutton(label='Green', underline=0, value=2,
                                   variable=self.selected_color,
                                   command=lambda: self.change_background_color('green'),
                                   accelerator='Ctr+G')
        color_menu.add_radiobutton(label='Blue', underline=0, value=3,
                                   variable=self.selected_color,
                                   command=lambda: self.change_background_color('blue'),
                                   accelerator='Ctr+B')
        self.menubar.add_cascade(label='Colors', menu=color_menu, underline=0)

    def binding_events(self):
        self.bind_all('<Shift-R>', lambda x: self.change_background_color('red'))
        self.bind_all('<Control-g>', lambda x: self.change_background_color('green'))
        self.bind_all('<Control-b>', lambda x: self.change_background_color('blue'))

    def change_background_color(self, color):
        self.configure(background=color)

if __name__ == '__main__':
    obj = LearnMenu()
    obj.mainloop()
