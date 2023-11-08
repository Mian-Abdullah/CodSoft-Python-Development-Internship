# Simple To-Do List in Python

# Initialize an empty list to store tasks
tasks = []


# Function to add a task to the list
def add_task(task):
    tasks.append(task)
    print("Task added:", task)


# Function to remove a task from the list by task number
def remove_task_by_number(task_number):
    if 1 <= task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print("Task removed:", removed_task)
    else:
        print("Invalid task number!")


# Function to remove a task from the list by task name
def remove_task_by_name(task_name):
    if task_name in tasks:
        tasks.remove(task_name)
        print("Task removed:", task_name)
    else:
        print("Task not found!")


# Function to display all tasks in the list
def display_tasks():
    print("Tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")


# Main function to interact with the user
def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Remove Task by Task Number")
        print("3. Remove Task by Task Name")
        print("4. Display Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            add_task(task)
        elif choice == "2":
            task_number = int(input("Enter the task number to remove: "))
            remove_task_by_number(task_number)
        elif choice == "3":
            task_name = input("Enter the task name to remove: ")
            remove_task_by_name(task_name)
        elif choice == "4":
            display_tasks()
        elif choice == "5":
            print("Exiting the to-do list. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# Run the main function
if __name__ == "__main__":
    main()
