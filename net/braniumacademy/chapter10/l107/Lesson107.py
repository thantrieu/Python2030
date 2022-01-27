import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


class LearnCheckbutton(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Learn Checkbutton Widget')
        self.geometry('300x150')
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.configure(pady=8, padx=8)
        self.create_widgets()
        self.drinks = set()

    def create_widgets(self):
        frm = ttk.Frame()
        self.coca = tk.IntVar()
        self.pepsi = tk.IntVar()
        self.water = tk.IntVar()
        self.milk = tk.IntVar()
        # add checkbutton
        self.check_coca = ttk.Checkbutton(frm, text='Coca cola',
                                          variable=self.coca,
                                          command=self.drink_change)
        self.check_coca.grid(row=0, column=0, sticky=tk.W)
        # add checkbox pepsi
        self.check_pepsi = ttk.Checkbutton(frm, text='Pepsi',
                                           variable=self.pepsi,
                                           command=self.drink_change)
        self.check_pepsi.grid(row=1, column=0, sticky=tk.W)

        self.check_milk = ttk.Checkbutton(frm, text='Milk',
                                          variable=self.milk,
                                          command=self.drink_change)
        self.check_milk.grid(row=2, column=0, sticky=tk.W)

        self.check_water = ttk.Checkbutton(frm, text='Water',
                                           variable=self.water,
                                           command=self.drink_change)
        self.check_water.grid(row=3, column=0, sticky=tk.W)
        # add button submit
        ttk.Button(frm, text='Done', command=self.submit).grid(row=4, column=0, sticky=tk.W, pady=8)
        frm.grid(row=0, column=1, sticky=tk.NSEW)

    def drink_change(self):
        if self.coca.get() == 1:
            self.drinks.add('Coca cola')
        elif 'Coca cola' in self.drinks:
            self.drinks.remove('Coca cola')
        # check whether pepsi checkbox is checked or unchecked
        if self.pepsi.get() == 1:
            self.drinks.add('Pepsi')
        elif 'Pepsi' in self.drinks:
            self.drinks.remove('Pepsi')
        # milk
        if self.milk.get() == 1:
            self.drinks.add('Milk')
        elif 'Milk' in self.drinks:
            self.drinks.remove('Milk')
        # water
        if self.water.get() == 1:
            self.drinks.add('Water')
        elif 'Water' in self.drinks:
            self.drinks.remove('Water')

    def submit(self):
        my_drink = ''
        for item in self.drinks:
            my_drink += item + '\n'
        showinfo(title='Your drink', message=my_drink)


if __name__ == '__main__':
    app = LearnCheckbutton()
    app.mainloop()
