import tkinter as tk
from tkinter import Menu


class LearnMenu(tk.Tk):
    def __init__(self):
        super(LearnMenu, self).__init__()
        self.title('Learn Menu')
        self.geometry('300x200')
        self.menubar = Menu()
        self.configure(menu=self.menubar)
        self.create_menus()

    def create_menus(self):
        file_menu = Menu(self.menubar, tearoff=False)
        file_menu.add_command(label='Open', underline=0)
        file_menu.add_command(label='Find', underline=0)
        file_menu.add_command(label='Close', underline=0)
        # add separator
        file_menu.add_separator()
        sub_menu = Menu(file_menu, tearoff=False)
        sub_menu.add_command(label='Theme')
        sub_menu.add_command(label='Font')
        sub_menu.add_command(label='Background Color')
        sub_menu.add_command(label='Window Size')
        file_menu.add_cascade(label='Preferences', menu=sub_menu)
        file_menu.add_separator()
        file_menu.add_command(label='Exit', command=self.destroy, underline=0)
        self.menubar.add_cascade(label='File', menu=file_menu, underline=0)
        # create help menu
        help_menu = Menu(self.menubar, tearoff=False)
        help_menu.add_command(label='Wecome')
        help_menu.add_command(label='About Us')
        self.menubar.add_cascade(label='Help', menu=help_menu, underline=0)
        # add menu color
        colors_menu = Menu(self.menubar, tearoff=False)
        self.checked = tk.IntVar()
        self.checked.trace_variable(mode='u', callback=self.change_background_color)
        colors_menu.add_radiobutton(label='Red', underline=0, accelerator='Shift+R',
                                    value=1, variable=self.checked,
                                    command=lambda: self.change_background_color(color='red'))
        colors_menu.add_radiobutton(label='Green', value=2, variable=self.checked,
                                    accelerator='Ctrl+G',
                                    command=lambda: self.change_background_color(color='green'))
        colors_menu.add_radiobutton(label='Blue', value=3, variable=self.checked,
                                    accelerator='Ctrl+B',
                                    command=lambda: self.change_background_color(color='blue'))
        self.menubar.add_cascade(label='Colors', menu=colors_menu, underline=0)
        self.menubar.bind_all('<Shift-R>', lambda x: self.change_background_color('red'))
        self.menubar.bind_all('<Control-b>', lambda x: self.change_background_color('blue'))
        self.menubar.bind_all('<Control-g>', lambda x: self.change_background_color('green'))

    def callback(self, event):
        print('Bind event')
        self.configure(background='red')

    def change_background_color(self, color='red'):
        self.configure(background=color)

    def location_change(self, event):
        pass


if __name__ == '__main__':
    obj = LearnMenu()
    obj.mainloop()
