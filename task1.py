import json
from datetime import datetime

# Function to load tasks from a file
def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Function to save tasks to a file
def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

# Function to add a task
def add_task(tasks):
    name = input("Enter the task name: ")
    priority = input("Enter the task priority (high/medium/low): ")
    due_date = input("Enter due date (DD-MM-YYYY): ")
    task = {"name": name, "priority": priority, "due_date": due_date, "completed": False}
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully.")

# Function to remove a task
def remove_task(tasks):
    index = int(input("Enter the index of the task to remove: "))
    if 0 <= index < len(tasks):
        del tasks[index]
        save_tasks(tasks)
        print("Task removed successfully.")
    else:
        print("Invalid index.")

# Function to mark a task as completed
def complete_task(tasks):
    index = int(input("Enter the index of the task to mark as completed: "))
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        save_tasks(tasks)
        print("Task marked as completed.")
    else:
        print("Invalid index.")

# Function to display all tasks
def display_tasks(tasks):
    for index, task in enumerate(tasks):
        print(f"{index}: {task['name']} (Priority: {task['priority']}, Due Date: {task['due_date']}, Completed: {task['completed']})")

# Main function
def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. Display Tasks")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            remove_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            display_tasks(tasks)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__== "__main__":
    main()
