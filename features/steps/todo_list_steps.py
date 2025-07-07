from behave import given, when, then
from todo_data import ToDoList

# GIVEN steps
@given('the to-do list is empty')
def step_impl(context):
    context.todo = ToDoList()

@given('the to-do list contains tasks:')
def step_impl(context):
    context.todo = ToDoList()
    for row in context.table:
        context.todo.add_task(row[0], "desc", "normal", "none")

@given('the to-do list contains tasks')
def step_impl(context):
    context.todo = ToDoList()
    for row in context.table:
        context.todo.add_task(row[0], "desc", "normal", "none")

@given('the to-do list contains task "{title}" as Pending')
def step_impl(context, title):
    context.todo = ToDoList()
    context.todo.add_task(title, "desc", "normal", "none")

@given('the to-do list contains task "{title}"')
def step_impl(context, title):
    context.todo = ToDoList()
    context.todo.add_task(title, "desc", "normal", "none")

# WHEN steps
@when('the user adds a task "{title}"')
def step_impl(context, title):
    context.todo.add_task(title, "desc", "normal", "none")

@when('the user adds tasks:')
def step_impl(context):
    for row in context.table:
        context.todo.add_task(row[0], "desc", "normal", "none")

@when('the user adds tasks')
def step_impl(context):
    for row in context.table:
        context.todo.add_task(row[0], "desc", "normal", "none")

@when('the user lists all tasks')
def step_impl(context):
    context.result = [task.title for task in context.todo.list_tasks()]

@when('the user marks task "{title}" as completed')
def step_impl(context, title):
    context.todo.mark_task_completed(title)

@when('the user clears the to-do list')
def step_impl(context):
    context.todo.clear_tasks()

@when('the user removes task "{title}"')
def step_impl(context, title):
    context.todo.remove_task(title)

# THEN steps
@then('the to-do list should contain "{title}"')
def step_impl(context, title):
    titles = [task.title for task in context.todo.list_tasks()]
    assert title in titles, f"Task '{title}' not found in to-do list"

@then('the output should contain:')
def step_impl(context):
    output_titles = [task.title for task in context.todo.list_tasks()]
    for row in context.table:
        assert row[0] in output_titles, f"Task '{row[0]}' not found in output"

@then('the output should contain')
def step_impl(context):
    output_titles = [task.title for task in context.todo.list_tasks()]
    for row in context.table:
        assert row[0] in output_titles, f"Task '{row[0]}' not found in output"

@then('the to-do list should be empty')
def step_impl(context):
    assert len(context.todo.list_tasks()) == 0, "To-do list is not empty"

@then('the task "{title}" should be marked as completed')
def step_impl(context, title):
    for task in context.todo.list_tasks():
        if task.title == title:
            assert task.completed, f"Task '{title}' is not marked as completed"
            return
    assert False, f"Task '{title}' not found"

@then('the to-do list should not contain "{title}"')
def step_impl(context, title):
    titles = [task.title for task in context.todo.list_tasks()]
    assert title not in titles, f"Task '{title}' should not be in to-do list"