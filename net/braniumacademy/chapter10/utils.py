import tkinter
from tkinter import N, S, W, E, CENTER
from tkinter import ttk


def clear_text(*args):
    label_result.configure(text='0')


def display(*args):
    # btn_0.cget('text')  # lấy text của một nút nào đó
    label_result.configure(text=btn_0.cget('text'))


root = tkinter.Tk()
root.minsize(320, 400)
root.maxsize(320, 400)
wwidth = root.winfo_width() / 4
wheight = root.winfo_height() / 7
root.title('Calculator')
frm = ttk.Frame(root, padding=16)
frm.place(anchor=CENTER, rely=0.5, relx=0.5)
frm.grid_propagate()
# frm.columnconfigure(0, weight=1)
# frm.rowconfigure(0, weight=1)
style = ttk.Style()
# style.configure('my.TButton', font=('Arial', 14))
# frm.grid_configure(sticky='NWES', padx=0.5, pady=0.5)
label_result = ttk.Label(frm, background='white', text='0', relief='ridge', border=2, font=('Arial', 18), anchor=E)
label_result.grid(row=0, column=0, columnspan=4, rowspan=1, sticky='NWSE', ipady=12, padx=8)
label_result.bind('<Enter>', lambda e: label_result.configure(text='Mouse moved inside'))
label_result.bind('<Leave>', lambda e: label_result.configure(text='Mouse moved outside'))
# label_result.configure(justify='center')
# label_result.rowconfigure(0, weight=1)
# label_result.columnconfigure(0, weight=1)
btn_mod = ttk.Button(frm, text='%')
btn_mod.grid(row=1, column=0, sticky='nswe')
# btn_mod.state(['disabled'])  # disable một nút
# btn_mod.configure(width=str(wwidth))
btn_clear = ttk.Button(frm, text='C', command=clear_text)
btn_clear.grid(row=1, column=1, sticky='nswe', ipady=16)
btn_del = ttk.Button(frm, text='DEL')
btn_del.grid(row=1, column=2, sticky='nswe')
btn_div = ttk.Button(frm, text='/')
btn_div.grid(row=1, column=3, sticky='nswe')
btn_7 = ttk.Button(frm, text='7')
btn_7.grid(row=2, column=0, sticky='nswe', ipady=16)
btn_8 = ttk.Button(frm, text='8')
btn_8.grid(row=2, column=1, sticky='nswe')
btn_9 = ttk.Button(frm, text='9')
btn_9.grid(row=2, column=2, sticky='nswe')
btn_4 = ttk.Button(frm, text='4')
btn_4.grid(row=3, column=0, sticky='nswe', ipady=16)
btn_5 = ttk.Button(frm, text='5')
btn_5.grid(row=3, column=1, sticky='nswe')
btn_6 = ttk.Button(frm, text='6')
btn_6.grid(row=3, column=2, sticky='nswe')
btn_1 = ttk.Button(frm, text='1')
btn_1.grid(row=4, column=0, sticky='nswe', ipady=16)
btn_2 = ttk.Button(frm, text='2')
btn_2.grid(row=4, column=1, sticky='nswe')
btn_3 = ttk.Button(frm, text='3')
btn_3.grid(row=4, column=2, sticky='nswe')
btn_0 = ttk.Button(frm, text='0', command=display)
btn_0.grid(row=5, column=1, sticky='nswe', ipady=16)
btn_sign = ttk.Button(frm, text='+/-')
btn_sign.grid(row=5, column=0, sticky='nswe')
btn_dot = ttk.Button(frm, text='.')
btn_dot.grid(row=5, column=2, sticky='nswe')
btn_equal = ttk.Button(frm, text='=')
btn_equal.grid(row=5, column=3, sticky='nswe')
btn_add = ttk.Button(frm, text='+')
btn_add.grid(row=4, column=3, sticky='nswe')
btn_sub = ttk.Button(frm, text='-')
btn_sub.grid(row=3, column=3, sticky='nswe')
btn_mul = ttk.Button(frm, text='*')
btn_mul.grid(row=2, column=3, sticky='nswe')

for e in frm.winfo_children():
    e.grid_configure(padx=2, pady=2)
    e.grid_configure()

root.mainloop()
