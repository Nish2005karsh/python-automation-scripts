import os

TASKS_FILE = "tasks.txt"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        tasks = [line.strip() for line in f.readlines()]
    return tasks

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("No tasks found. Time to chill! 😎")
    else:
        for idx, task in enumerate(tasks, 1):
            status = "[x]" if task.startswith("[x]") else "[ ]"
            task_text = task[3:] if task.startswith("[x]") or task.startswith("[ ]") else task
            print(f"{idx}. {status} {task_text}")

def add_task(tasks):
    task = input("Enter your new task: ").strip()
    if task:
        tasks.append("[ ] " + task)
        print(f'Added task: "{task}"')
    else:
        print("Task cannot be empty!")

def complete_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Enter the task number to mark as complete: "))
        if 1 <= num <= len(tasks):
            tasks[num-1] = "[x] " + tasks[num-1][3:]
            print("Task marked as complete!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Enter the task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num-1)
            print(f'Removed task: "{removed[3:]}"')
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = load_tasks()
    while True:
        print("\n--- CLI Task Manager ---")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
            save_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
            save_tasks(tasks)
        elif choice == "4":
            delete_task(tasks)
            save_tasks(tasks)
        elif choice == "5":
            print("Bye! Stay productive! 👋")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
