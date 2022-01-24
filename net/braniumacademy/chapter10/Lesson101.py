import tkinter
from tkinter import ttk

root = tkinter.Tk()
root.title('Tkinter GUI Example')
root.geometry('400x300')
frm = ttk.Frame(root, padding=10)
frm.place(anchor=tkinter.CENTER, relx=0.5, rely=0.5)
label_hello = ttk.Label(frm, text='Hello World!', font=('Arial', 24), foreground='red')
label_hello.grid(row=0, column=0)
btn_exit = ttk.Button(frm, text='Quit', command=root.destroy)
btn_exit.grid(row=1, column=0)
root.mainloop()
