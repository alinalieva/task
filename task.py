class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Not Completed"
        return f"Title: {self.title}\nDescription: {self.description}\nStatus: {status}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def complete_task(self, index):
        if index >= 0 and index < len(self.tasks):
            task = self.tasks[index]
            task.mark_as_completed()
            print(f"Task '{task.title}' marked as completed.")
        else:
            print("Invalid task index.")

    def display_tasks(self):
        if len(self.tasks) == 0:
            print("No tasks to display.")
        else:
            print("Tasks:")
            for i, task in enumerate(self.tasks):
                print(f"Task {i+1}:\n{task}\n")

    def __str__(self):
        return f"TaskManager: {len(self.tasks)} tasks"


# Create a TaskManager instance
task_manager = TaskManager()

# Add tasks
task1 = Task("Complete project", "Finish coding and testing.")
task2 = Task("Buy groceries", "Get milk, eggs, and bread.")
task3 = Task("Exercise", "Go for a 30-minute jog.")
task_manager.add_task(task1)
task_manager.add_task(task2)
task_manager.add_task(task3)

# Display tasks
task_manager.display_tasks()

# Complete a task
task_manager.complete_task(1)

# Display tasks after completion
task_manager.display_tasks()
