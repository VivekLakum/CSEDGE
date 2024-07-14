import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry_task.get()
    if task != "":
        list_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def delete_task():
    try:
        selected_index = list_tasks.curselection()[0]
        list_tasks.delete(selected_index)
        save_tasks()
    except:
        messagebox.showwarning("Warning", "You must select a task to delete.")

def mark_task_completed():
    try:
        selected_index = list_tasks.curselection()[0]
        task = list_tasks.get(selected_index)
        list_tasks.delete(selected_index)
        list_tasks.insert(tk.END, task + " (completed)")
        save_tasks()
    except:
        messagebox.showwarning("Warning", "You must select a task to mark as completed.")

def mark_task_priority():
    try:
        selected_index = list_tasks.curselection()[0]
        task = list_tasks.get(selected_index)
        list_tasks.delete(selected_index)
        list_tasks.insert(0, task + " (priority)")
        save_tasks()
    except:
        messagebox.showwarning("Warning", "You must select a task to mark as priority.")

def save_tasks():
    with open("tasks.txt", "w") as file:
        tasks = list_tasks.get(0, tk.END)
        for task in tasks:
            file.write(task + "\n")

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            for task in tasks:
                list_tasks.insert(tk.END, task.strip())
    except FileNotFoundError:
        pass

def on_enter(e):
    e.widget['background'] = '#ff3333'

def on_leave(e):
    e.widget['background'] = '#ff6666'

root = tk.Tk()
root.title("To-Do List")
root.geometry("400x500")
root.configure(bg='#333333')

canvas = tk.Canvas(root, width=400, height=500)
canvas.grid(row=0, column=0)

colors = ["#ffcccc", "#ff99cc", "#ff66cc", "#ff33cc", "#ff00cc", "#cc00cc"]
for i, color in enumerate(colors):
    canvas.create_rectangle(0, i*500//len(colors), 400, (i+1)*500//len(colors), fill=color, outline="")

frame = tk.Frame(root, bg='#333333')
frame.place(relwidth=0.95, relheight=0.9, relx=0.025, rely=0.025)

entry_task = tk.Entry(frame, width=30, font=('Helvetica', 14), borderwidth=2, relief='solid')
entry_task.pack(padx=20, pady=10)

button_add = tk.Button(frame, text="Add Task", command=add_task, bg='#ff9999', fg='#ffffff', font=('Helvetica', 14, 'bold'), borderwidth=2, relief='raised')
button_add.pack(pady=5)

button_delete = tk.Button(frame, text="Delete Task", command=delete_task, bg='#ff6666', fg='#ffffff', font=('Helvetica', 14, 'bold'), borderwidth=2, relief='raised')
button_delete.pack(pady=5)

button_completed = tk.Button(frame, text="Mark Completed", command=mark_task_completed, bg='#66cc66', fg='#ffffff', font=('Helvetica', 14, 'bold'), borderwidth=2, relief='raised')
button_completed.pack(pady=5)

button_priority = tk.Button(frame, text="Mark Priority", command=mark_task_priority, bg='#ffcc00', fg='#ffffff', font=('Helvetica', 14, 'bold'), borderwidth=2, relief='raised')
button_priority.pack(pady=5)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
list_tasks = tk.Listbox(frame, width=50, height=10, font=('Helvetica', 14), bg='#ffffff', fg='#333333', selectbackground='#ff9999', selectforeground='#ffffff', borderwidth=2, relief='solid', yscrollcommand=scrollbar.set)
list_tasks.pack(pady=20)
scrollbar.config(command=list_tasks.yview)

button_add.bind("<Enter>", on_enter)
button_add.bind("<Leave>", on_leave)
button_delete.bind("<Enter>", on_enter)
button_delete.bind("<Leave>", on_leave)
button_completed.bind("<Enter>", on_enter)
button_completed.bind("<Leave>", on_leave)
button_priority.bind("<Enter>", on_enter)
button_priority.bind("<Leave>", on_leave)

load_tasks()

root.mainloop()

