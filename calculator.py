import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Calculator")

def add():
    try:
        result = float(entry_num1.get()) + float(entry_num2.get())
        label_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers!")

def subtract():
    try:
        result = float(entry_num1.get()) - float(entry_num2.get())
        label_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers!")

def multiply():
    try:
        result = float(entry_num1.get()) * float(entry_num2.get())
        label_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers!")

def divide():
    try:
        if float(entry_num2.get()) == 0:
            messagebox.showerror("Math Error", "Division by zero is not allowed!")
        else:
            result = float(entry_num1.get()) / float(entry_num2.get())
            label_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers!")

def clear():
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)
    label_result.config(text="Result:")


entry_num1 = tk.Entry(root, width=20)
entry_num1.grid(row=0, column=1, pady=5)
tk.Label(root, text="Number 1:").grid(row=0, column=0, pady=5)

entry_num2 = tk.Entry(root, width=20)
entry_num2.grid(row=1, column=1, pady=5)
tk.Label(root, text="Number 2:").grid(row=1, column=0, pady=5)

label_result = tk.Label(root, text="Result:", font=("Arial", 14))
label_result.grid(row=2, column=0, columnspan=2, pady=10)

btn_multiply = tk.Button(root, text="*", width=5, command=multiply)
btn_multiply.grid(row=3, column=0, pady=5)

btn_divide = tk.Button(root, text="/", width=5, command=divide)
btn_divide.grid(row=3, column=1, pady=5)

btn_add = tk.Button(root, text="+", width=5, command=add)
btn_add.grid(row=4, column=0, pady=5)

btn_subtract = tk.Button(root, text="-", width=5, command=subtract)
btn_subtract.grid(row=4, column=1, pady=5)

btn_clear = tk.Button(root, text="CLEAR", width=10, command=clear)
btn_clear.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()