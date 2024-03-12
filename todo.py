# class TodoList:
#     def __init__(self):
#         self.tasks = []

#     def add_task(self, task):
#         self.tasks.append(task)

#     def remove_task(self, task_index):
#         del self.tasks[task_index]

#     def display_tasks(self):
#         if not self.tasks:
#             print("No tasks.")
#         else:
#             for i, task in enumerate(self.tasks):
#                 print(f"{i + 1}. {task}")

#     def update_task(self, task_index, new_task):
#         self.tasks[task_index] = new_task


# def main():
#     todo_list = TodoList()

#     while True:
#         print("\n1. Add Task")
#         print("2. Remove Task")
#         print("3. View Tasks")
#         print("4. Update Task")
#         print("5. Exit")

#         choice = input("Enter your choice: ")

#         if choice == '1':
#             task = input("Enter task: ")
#             todo_list.add_task(task)
#         elif choice == '2':
#             if todo_list.tasks:
#                 todo_list.display_tasks()
#                 task_index = int(input("Enter task number to remove: ")) - 1
#                 todo_list.remove_task(task_index)
#             else:
#                 print("No tasks to remove.")
#         elif choice == '3':
#             todo_list.display_tasks()
#         elif choice == '4':
#             if todo_list.tasks:
#                 todo_list.display_tasks()
#                 task_index = int(input("Enter task number to update: ")) - 1
#                 new_task = input("Enter new task: ")
#                 todo_list.update_task(task_index, new_task)
#             else:
#                 print("No tasks to update.")
#         elif choice == '5':
#             print("Exiting program.")
#             break
#         else:
#             print("Invalid choice. Please try again.")


# if __name__ == "__main__":
#     main()
import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        
        self.tasks = []

        self.task_var = tk.StringVar()
        self.task_entry = tk.Entry(root, textvariable=self.task_var, width=40)
        self.task_entry.grid(row=0, column=0, padx=5, pady=5)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=5, pady=5)

        self.listbox = tk.Listbox(root, width=50)
        self.listbox.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        self.remove_button.grid(row=2, column=0, padx=5, pady=5)

        self.clear_button = tk.Button(root, text="Clear All", command=self.clear_tasks)
        self.clear_button.grid(row=2, column=1, padx=5, pady=5)

    def add_task(self):
        task = self.task_var.get()
        if task:
            self.tasks.append(task)
            self.listbox.insert(tk.END, task)
            self.task_var.set("")
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    def remove_task(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            idx = selected_index[0]
            self.listbox.delete(idx)
            del self.tasks[idx]

    def clear_tasks(self):
        self.listbox.delete(0, tk.END)
        self.tasks.clear()

def main():
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
