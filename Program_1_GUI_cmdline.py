import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import datetime

class Task:
    def __init__(self, description, due_date=None, task_priority="Normal"):
        self.description = description
        self.due_date = due_date
        self.task_priority = task_priority
        self.completed = False

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.description} (Due: {self.due_date}, Priority: {self.task_priority})"


class TaskHandler:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date=None, task_priority="Normal"):
        task = Task(description, due_date, task_priority)
        self.tasks.append(task)

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]

    def update_task(self, index, new_description, new_due_date=None, new_priority="Normal"):
        if 0 <= index < len(self.tasks):
            self.tasks[index].description = new_description
            self.tasks[index].due_date = new_due_date
            self.tasks[index].task_priority = new_priority

    def move_task_up(self, index):
        if 0 < index < len(self.tasks):
            self.tasks[index], self.tasks[index - 1] = self.tasks[index - 1], self.tasks[index]

    def move_task_down(self, index):
        if 0 <= index < len(self.tasks) - 1:
            self.tasks[index], self.tasks[index + 1] = self.tasks[index + 1], self.tasks[index]

    def get_tasks(self):
        return self.tasks


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")

        # Configure the grid to allow for flexible resizing
        self.root.grid_rowconfigure(0, weight=1)  # Title row
        self.root.grid_rowconfigure(1, weight=1)  # Task list row
        self.root.grid_rowconfigure(2, weight=0)  # Button rows
        self.root.grid_rowconfigure(3, weight=0)
        self.root.grid_rowconfigure(4, weight=0)
        
        self.root.grid_columnconfigure(0, weight=1)  # All columns can expand
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)

        self.title_label = tk.Label(self.root, text="My TO-DO LIST", font=("Helvetica", 16))
        self.title_label.grid(row=0, column=0, columnspan=3, pady=10)

        self.task_manager = TaskHandler()

        self.task_listbox = tk.Listbox(self.root, width=60, height=15)
        self.task_listbox.grid(row=1, column=0, columnspan=3, pady=20, sticky='nsew')

        # Add buttons to a grid layout
        self.add_task_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_task_button.grid(row=2, column=0, pady=5, sticky='ew')

        self.remove_task_button = tk.Button(self.root, text="Remove Task", command=self.task_remover)
        self.remove_task_button.grid(row=2, column=1, pady=5, sticky='ew')

        self.update_task_button = tk.Button(self.root, text="Mark as Completed", command=self.task_updater)
        self.update_task_button.grid(row=2, column=2, pady=5, sticky='ew')

        self.edit_task_button = tk.Button(self.root, text="Edit Task", command=self.task_editor)
        self.edit_task_button.grid(row=3, column=0, pady=5, sticky='ew')

        # Updated buttons for moving tasks up and down with arrows
        self.move_up_button = tk.Button(self.root, text="↑ Move Up", command=self.move_task_up)
        self.move_up_button.grid(row=3, column=1, pady=5, sticky='ew')

        self.move_down_button = tk.Button(self.root, text="↓ Move Down", command=self.move_task_down)
        self.move_down_button.grid(row=3, column=2, pady=5, sticky='ew')

        self.load_button = tk.Button(self.root, text="Load Tasks", command=self.load_tasks)
        self.load_button.grid(row=4, column=0, pady=5, sticky='ew')

        self.save_button = tk.Button(self.root, text="Save Tasks", command=self.save_tasks)
        self.save_button.grid(row=4, column=1, pady=5, sticky='ew')

        self.exit_button = tk.Button(self.root, text="Exit", command=self.exit_app)
        self.exit_button.grid(row=4, column=2, pady=5, sticky='ew')

    def add_task(self):
        description = simpledialog.askstring("Task Description", "Enter the task description:")
        due_date = simpledialog.askstring("Due Date", "Enter due date (DD-MM-YYYY, optional):")
        priority = simpledialog.askstring("Priority", "Enter priority (High, Medium, Low, Normal):")

        if description:
            if due_date:
                try:
                    datetime.strptime(due_date, "%d-%m-%Y")  # Validate date format
                except ValueError:
                    messagebox.showwarning("Date Error", "Please enter a valid date (DD-MM-YYYY).")
                    return

            task_priority = priority if priority else "Normal"
            self.task_manager.add_task(description, due_date, task_priority)
            self.update_task_list()

    def task_remover(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.task_manager.remove_task(selected_index)
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to remove.")

    def task_updater(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            current_task = self.task_manager.get_tasks()[selected_index]
            current_task.completed = not current_task.completed
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to update.")

    def task_editor(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            current_task = self.task_manager.get_tasks()[selected_index]

            new_description = simpledialog.askstring("Edit Task", "Enter new task description:", initialvalue=current_task.description)
            new_due_date = simpledialog.askstring("Due Date", "Enter new due date (DD-MM-YYYY, optional):", initialvalue=current_task.due_date)
            new_priority = simpledialog.askstring("Priority", "Enter new priority (High, Medium, Low, Normal):", initialvalue=current_task.task_priority)

            if new_description:
                if new_due_date:
                    try:
                        datetime.strptime(new_due_date, "%d-%m-%Y")  # Validate date format
                    except ValueError:
                        messagebox.showwarning("Date Error", "Please enter a valid date (DD-MM-YYYY).")
                        return

                self.task_manager.update_task(selected_index, new_description, new_due_date, new_priority)
                self.update_task_list()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to edit.")

    def move_task_up(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.task_manager.move_task_up(selected_index)
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to move up.")

    def move_task_down(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.task_manager.move_task_down(selected_index)
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to move down.")

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.task_manager.get_tasks():
            self.task_listbox.insert(tk.END, str(task))

    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.task_manager.get_tasks():
                file.write(f"{task.description}|{task.due_date}|{task.task_priority}|{task.completed}\n")
        messagebox.showinfo("Success", "Tasks saved to tasks.txt.")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                for line in file:
                    description, due_date, priority, completed = line.strip().split("|")
                    completed = completed == "True"
                    task = Task(description, due_date if due_date != "None" else None, priority)
                    task.completed = completed
                    self.task_manager.tasks.append(task)
            self.update_task_list()
            messagebox.showinfo("Success", "Tasks loaded from tasks.txt.")
        except FileNotFoundError:
            messagebox.showwarning("File Not Found", "No tasks to load.")

    def exit_app(self):
        if messagebox.askokcancel("Quit", "Do you want to quit the application?"):
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
