import tkinter as tk 

def click(button):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + button)

def evaluate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def clear():
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Basic Calculator")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

entry = tk.Entry(frame, width=16, font=('Helvetica', 24, 'bold'), borderwidth=2, relief='solid', bg='#ffffff', fg='#333333', justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

buttons = [
    ('7', '#000000', '#ffffff'), ('8', '#000000', '#ffffff'), ('9', '#000000', '#ffffff'), ('/', '#ff9999', '#000000'),
    ('4', '#000000', '#ffffff'), ('5', '#000000', '#ffffff'), ('6', '#000000', '#ffffff'), ('*', '#ff9999', '#000000'),
    ('1', '#000000', '#ffffff'), ('2', '#000000', '#ffffff'), ('3', '#000000', '#ffffff'), ('-', '#ff9999', '#000000'),
    ('0', '#000000', '#ffffff'), ('C', '#ffcc99', '#000000'), ('=', '#ffcc99', '#000000'), ('+', '#ff9999', '#000000'),
]

row_val = 1
col_val = 0

for (button_text, bg_color, fg_color) in buttons:
    if button_text == "=":
        btn = tk.Button(frame, text=button_text, width=4, height=2, font=('Helvetica', 18, 'bold'), command=evaluate, bg=bg_color, fg=fg_color, borderwidth=2, relief='raised')
    elif button_text == "C":
        btn = tk.Button(frame, text=button_text, width=4, height=2, font=('Helvetica', 18, 'bold'), command=clear, bg=bg_color, fg=fg_color, borderwidth=2, relief='raised')
    else:
        btn = tk.Button(frame, text=button_text, width=4, height=2, font=('Helvetica', 18, 'bold'), command=lambda b=button_text: click(b), bg=bg_color, fg=fg_color, borderwidth=2, relief='raised')

    btn.grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
