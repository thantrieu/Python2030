from tkinter import *
from tkinter import ttk
root = Tk()
root.geometry('400x400')
# frm = ttk.Frame(root, padding=10, width=400, height=400)
# frm.place(rely=0.5, relx=0.5, anchor=CENTER)
# frm.configure(borderwidth=5)
# frm.grid()
ttk.Label(root, text="Hello Meow!", foreground='green', font=('Arial', 25)).place(rely=0.5, relx=0.5, anchor=CENTER)
ttk.Button(root, text="Quit", command=root.destroy).place(rely=0.5, relx=0.5, anchor=CENTER)
root.mainloop()

# import tkinter
# from tkinter import ttk, S, N, W, E
# window = tkinter.Tk()
# window.grid()
# window.title('First Python GUI')
# # window.minsize(width=400, height=300)
# # window.maxsize(width=800, height=600)
# mainframe = ttk.Frame(window, padding='3 3 12 12')
# mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
# window.rowconfigure(0, weight=5)
# window.columnconfigure(0, weight=1)
# ttk.Button(mainframe, text='Click Me').grid(column=3, row=3, sticky=W)
# window.geometry('400x400')
# window.configure(background='green', cursor='fleur')
# window.mainloop()
