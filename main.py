

tasks = [] # list to store tasks
file_path = "tasks.txt" # file path to save tasks

# function to add task
def load_tasks():
    try:
        with open(file_path, "r") as file:
            for line in file:
                tasks.append(line.strip())
    except FileNotFoundError:
        open(file_path, "w").close()  # Create file if not exists

# Save tasks to the file
def save_tasks():
    with open(file_path, "w") as file:
        for task in tasks:
            file.write(task + "\n")


# function to add task
def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    save_tasks()
    print("✅ Task added!")

# function to remove a task
def remove_task():
    view_tasks()
    try:
        index = int(input("Enter task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks()
            print(f"❌ Removed: {removed}")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a number.")


# function to View task.
def view_tasks():
    if not tasks:
        print("📭 No tasks yet.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")


def menu():
    load_tasks()
    while True:
        print("\n--- To-Do CLI Menu ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            print("👋 Exiting To-Do App.")
            break
        else:
            print("⚠️ Invalid choice.")

if __name__ == "__main__":
    menu()