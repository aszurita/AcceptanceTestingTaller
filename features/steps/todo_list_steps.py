from behave import given, when, then
from features.steps.todo_list_mock import todo_list

@given('the to-do list is empty')
def step_impl(context):
    todo_list.clear_tasks()

@when('the user adds a task "{task}"')
def step_impl(context, task):
    todo_list.add_task(task)

@then('the to-do list should contain "{task}"')
def step_impl(context, task):
    tasks = todo_list.list_tasks()
    assert any(task in t for t in tasks)

@given('the to-do list contains tasks:')
def step_impl(context):
    todo_list.clear_tasks()
    for row in context.table:
        todo_list.add_task(row['Task'])

@given('the to-do list contains tasks with status:')
def step_impl(context):
    todo_list.clear_tasks()
    for row in context.table:
        todo_list.add_task(row['Task'])
        if row['Status'] == "Completed":
            todo_list.complete_task(row['Task'])

@when('the user lists all tasks')
def step_impl(context):
    context.output = todo_list.list_tasks()

@then('the output should contain:')
def step_impl(context):
    for row in context.table:
        assert any(row['Task'] in t for t in context.output)

@when('the user marks task "{task}" as completed')
def step_impl(context, task):
    todo_list.complete_task(task)

@then('the task "{task}" should show as completed')
def step_impl(context, task):
    t = todo_list.get_task(task)
    assert t is not None and t.status == "Completed"

@when('the user clears the to-do list')
def step_impl(context):
    todo_list.clear_tasks()

@then('the to-do list should be empty')
def step_impl(context):
    assert todo_list.is_empty()
