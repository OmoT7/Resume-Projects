import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry = ('1000x2000')
root.resizable = (True, True)

root.title('Calculator')

expression = ""

def press(num):
    global expression

    expression = expression + str(num)
    expression_field.delete(0, tk.END)
    expression_field.insert(0, expression)
def add():
    global expression
    expression = expression + '+'
    expression_field.delete(0, tk.END)
    expression_field.insert(0, expression)
def sub():
    global expression
    expression = expression + '-'
    expression_field.delete(0, tk.END)
    expression_field.insert(0, expression)
def multi():
    global expression
    expression = expression + '*'
    expression_field.delete(0, tk.END)
    expression_field.insert(0, expression)
def divide():
    global expression
    expression = expression + '/'
    expression_field.delete(0, tk.END)
    expression_field.insert(0, expression)


def equal():
    try:
        global expression

        total = str(eval(expression))
        expression_field.delete(0, tk.END)
        expression_field.insert(0, total)
        expression = total
        
    except:

        expression_field.delete(0, tk.END)
        expression_field.insert(0, "ERROR")

def clear():
    global expression

    expression_field.delete(0, tk.END)
    expression = ""
    
"""
# exit button
exit_button = ttk.Button(
    root,
    text='Exit',
    command=lambda: root.quit()
)

exit_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)
"""

root.columnconfigure(0, weight=5)
root.columnconfigure(1, weight=5)

button_0 = ttk.Button(root, text='0', command= lambda: press(0))
button_1 = ttk.Button(root, text='1', command= lambda: press(1))
button_2 = ttk.Button(root, text='2', command= lambda: press(2))
button_3 = ttk.Button(root, text='3', command= lambda: press(3))
button_4 = ttk.Button(root, text='4', command= lambda: press(4))
button_5 = ttk.Button(root, text='5', command= lambda: press(5))
button_6 = ttk.Button(root, text='6', command= lambda: press(6))
button_7 = ttk.Button(root, text='7', command= lambda: press(7))
button_8 = ttk.Button(root, text='8', command= lambda: press(8))
button_9 = ttk.Button(root, text='9', command= lambda: press(9))
button_clear = ttk.Button(root, text='C', command= clear)
button_equal = ttk.Button(root, text='=', command= equal)

button_add = ttk.Button(root, text='+', command= add)
button_sub = ttk.Button(root, text='-', command= sub)
button_mult = ttk.Button(root, text='*', command = multi)
button_div = ttk.Button(root, text='/', command= divide)

button_clear.grid(column=1, row=5, sticky=tk.E, padx=5, pady=5)
button_0.grid(column=2, row=5, sticky=tk.E, padx=5, pady=5)
button_equal.grid(column=3, row=5, sticky=tk.E, padx=5, pady=5)

button_1.grid(column=1, row=4, sticky=tk.E, padx=5, pady=5)
button_2.grid(column=2, row=4, sticky=tk.E, padx=5, pady=5)
button_3.grid(column=3, row=4, sticky=tk.E, padx=5, pady=5)

button_4.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)
button_5.grid(column=2, row=3, sticky=tk.E, padx=5, pady=5)
button_6.grid(column=3, row=3, sticky=tk.E, padx=5, pady=5)

button_7.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)
button_8.grid(column=2, row=2, sticky=tk.E, padx=5, pady=5)
button_9.grid(column=3, row=2, sticky=tk.E, padx=5, pady=5)

equation = expression

expression_field = ttk.Entry(root, textvariable=equation)

expression_field.grid(row=1, columnspan=5, ipadx=100)


button_add.grid(column=4, row=2, sticky=tk.E, padx=5, pady=5)
button_sub.grid(column=4, row=3, sticky=tk.E, padx=5, pady=5)
button_mult.grid(column=4, row=4, sticky=tk.E, padx=5, pady=5)
button_div.grid(column=4, row=5, sticky=tk.E, padx=5, pady=5)


root.mainloop()