# todo_list.py
from todo_data import ToDoList

todo = ToDoList()

def show_menu():
    print("\n1. Add Task")
    print("2. List Tasks")
    print("3. Mark Task Completed")
    print("4. Clear All Tasks")
    print("5. Remove Task")
    print("6. Exit")

while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        title = input("Title: ")
        description = input("Description: ")
        priority = input("Priority: ")
        due_date = input("Due Date: ")
        todo.add_task(title, description, priority, due_date)

    elif choice == "2":
        tasks = todo.list_tasks()
        for task in tasks:
            status = "Done" if task.completed else "Pending"
            print(f"- {task.title} | {status} | {task.description} | Priority: {task.priority} | Due: {task.due_date}")

    elif choice == "3":
        title = input("Title to mark completed: ")
        todo.mark_task_completed(title)

    elif choice == "4":
        todo.clear_tasks()

    elif choice == "5":
        title = input("Title to remove: ")
        todo.remove_task(title)

    elif choice == "6":
        break

    else:
        print("Invalid option.")
