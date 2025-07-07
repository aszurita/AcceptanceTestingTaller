Feature: To-Do List Management

  Scenario: Add a task
    Given the to-do list is empty
    When the user adds a task "Buy groceries"
    Then the to-do list should contain "Buy groceries"

  Scenario: List all tasks
    Given the to-do list contains tasks:
      | Buy groceries |
      | Pay bills |
    When the user lists all tasks
    Then the output should contain:
      | Buy groceries |
      | Pay bills |

  Scenario: Mark task as completed
    Given the to-do list contains task "Buy groceries" as Pending
    When the user marks task "Buy groceries" as completed
    Then the task "Buy groceries" should be marked as completed

  Scenario: Clear the to-do list
    Given the to-do list contains tasks:
      | Buy groceries |
      | Pay bills |
    When the user clears the to-do list
    Then the to-do list should be empty

  Scenario: Remove a task
    Given the to-do list contains task "Call mom"
    When the user removes task "Call mom"
    Then the to-do list should not contain "Call mom"

  Scenario: Add multiple tasks and list them
    Given the to-do list is empty
    When the user adds tasks:
      | Study |
      | Exercise |
    Then the output should contain:
      | Study |
      | Exercise |