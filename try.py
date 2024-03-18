class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def update_task(self, task_index,updated_task):
        if 1<= task_index <= len(self.tasks):
            self.tasks[task_index -1]["task"] =updated_task
            print("Task added sucessfully")
        else:
            print("Invalid task index")

    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]
        else:
            print("Invalid task index")

    def display_tasks(self):
        if self.tasks:
            print("To-Do List:")
            for index, task in enumerate(self.tasks):
                status = "X" if task["completed"] else " "
                print(f"{index + 1}. [{status}] {task['task']}")
        else:
            print("No tasks in the to-do list.")


def main():
    todo_list = TodoList()

    while True:
        print("\nWhat would you like to do?")
        print("1. Add a task")
        print("2. Update a task")
        print("3. Remove a task")
        print("4. View tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
            print("Task added successfully.")
        elif choice == "2":
            task_index = int(input("Enter the index of the task to update: "))
            updated_task = input("Enter the updated task: ")
            todo_list.update_task(task_index, updated_task)
            print("Task updated sucessfully.")
        elif choice == "3":
            task_index = int(input("Enter the index of the task to remove: ")) 
            todo_list.remove_task(task_index)
            print("Task removed successfully.")
        elif choice == "4":
            todo_list.display_tasks()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()

