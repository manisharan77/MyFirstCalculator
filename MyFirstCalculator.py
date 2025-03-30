import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        result = eval(entry.get())  # Be cautious with eval()!
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Main window
window = tk.Tk()
window.title("Calculator")

# Entry widget
entry = tk.Entry(window, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Buttons
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

row_val = 1
col_val = 0

for button in buttons:
    if button == "=":
        tk.Button(window, text=button, padx=40, pady=20, command=button_equal).grid(row=row_val, column=col_val)
    elif button == "C":
        tk.Button(window, text="C", padx=40, pady=20, command=button_clear).grid(row=row_val, column=col_val)
    else:
        tk.Button(window, text=button, padx=40, pady=20, command=lambda b=button: button_click(b)).grid(row=row_val, column=col_val)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Clear button.
tk.Button(window, text="C", padx=40, pady=20, command=button_clear).grid(row=5, column=0)

window.mainloop()