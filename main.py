import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    expression = entry.get()
    try:
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create an entry widget to display the calculations
entry = tk.Entry(window, width=30, justify=tk.RIGHT, font=('Arial', 14))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create number buttons
buttons = []
for i in range(9):
    button = tk.Button(window, text=str(i + 1), padx=20, pady=10, font=('Arial', 12),
                       command=lambda num=i+1: button_click(num))
    buttons.append(button)
    buttons[i].grid(row=3 - (i // 3), column=i % 3, padx=5, pady=5)

# Create operator buttons
operators = ['+', '-', '*', '/']
for i, operator in enumerate(operators):
    button = tk.Button(window, text=operator, padx=20, pady=10, font=('Arial', 12),
                       command=lambda op=operator: button_click(op))
    buttons.append(button)
    buttons[-1].grid(row=i+1, column=3, padx=5, pady=5)

# Create clear button
clear_button = tk.Button(window, text="C", padx=20, pady=10, font=('Arial', 12), command=button_clear)
clear_button.grid(row=4, column=0, padx=5, pady=5)

# Create equal button
equal_button = tk.Button(window, text="=", padx=20, pady=10, font=('Arial', 12), command=button_equal)
equal_button.grid(row=4, column=1, padx=5, pady=5)

# Start the GUI main loop
window.mainloop()
