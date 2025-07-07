class Task:
    def __init__(self, title, description, priority, due_date):
        self.title = title
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.completed = False

    def mark_completed(self):
        self.completed = True

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, priority, due_date):
        task = Task(title, description, priority, due_date)
        self.tasks.append(task)

    def list_tasks(self):
        return self.tasks

    def mark_task_completed(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_completed()
                return True
        return False

    def clear_tasks(self):
        self.tasks = []

    def remove_task(self, title):
        self.tasks = [task for task in self.tasks if task.title != title]
