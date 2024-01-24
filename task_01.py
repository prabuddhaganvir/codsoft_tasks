import os

def display_menu():
    print("\nMenu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Remove Task")
    print("5. Exit")

def add_task(task, task_file):
    with open(task_file, 'a') as file:
        file.write(task + '\n')

def view_tasks(task_file):
    if os.path.exists(task_file):
        with open(task_file, 'r') as file:
            tasks = file.readlines()
            if not tasks:
                print("No tasks in the to-do list.")
            else:
                print("To-Do List:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task.strip()}")
    else:
        print("No tasks in the to-do list.")

def mark_completed(task_number, task_file):
    tasks = []
    if os.path.exists(task_file):
        with open(task_file, 'r') as file:
            tasks = file.readlines()
    
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1] = "[Done] " + tasks[task_number - 1]

        with open(task_file, 'w') as file:
            file.writelines(tasks)

        print(f"Task {task_number} marked as completed.")
    else:
        print("Invalid task number.")

def remove_task(task_number, task_file):
    tasks = []
    if os.path.exists(task_file):
        with open(task_file, 'r') as file:
            tasks = file.readlines()

    if 1 <= task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)

        with open(task_file, 'w') as file:
            file.writelines(tasks)

        print(f"Task {task_number} removed: {removed_task.strip()}")
    else:
        print("Invalid task number.")

# Main program
task_file = "todo_list.txt"

while True:
    display_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        task = input("Enter the task: ")
        add_task(task, task_file)
    elif choice == "2":
        view_tasks(task_file)
    elif choice == "3":
        task_number = int(input("Enter the task number to mark as completed: "))
        mark_completed(task_number, task_file)
    elif choice == "4":
        task_number = int(input("Enter the task number to remove: "))
        remove_task(task_number, task_file)
    elif choice == "5":
        print("Exiting the to-do list application. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
