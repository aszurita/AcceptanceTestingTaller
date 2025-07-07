class Task:
    def __init__(self, name, status="Pending", priority="Normal", due_date=None):
        self.name = name
        self.status = status
        self.priority = priority
        self.due_date = due_date

    def complete(self):
        self.status = "Completed"

    def __str__(self):
        return f"{self.name} [{self.status}]"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, name):
        self.tasks.append(Task(name))

    def list_tasks(self):
        return [str(task) for task in self.tasks]

    def complete_task(self, name):
        for task in self.tasks:
            if task.name == name:
                task.complete()

    def clear_tasks(self):
        self.tasks = []

    def is_empty(self):
        return len(self.tasks) == 0

    def get_task(self, name):
        return next((task for task in self.tasks if task.name == name), None)


# Singleton for testing
todo_list = ToDoList()
