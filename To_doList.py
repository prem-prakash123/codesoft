import os

def main():
    print("___To-Do- list___")
    print("1. Show Tasks")
    print("2. Add Tasks")
    print("3.Update Tasks")
    print("4. Delete Tasks")
    print("5. Exit")
    choice =int(input("Enter your choice(1-5): "))
    if choice== 1:
        show_task(tasks)
    elif choice == 2:
        new_task =input("Enter the task to add: ")
        add_task(task, new_task)
    elif choice == 3:
        index =int(input("Enter the task index to update: "))
        updated_task = input("Enter the task: ")
        update_task(task, index, updated_task)
    elif choice == 4:
        index =int(index("Enter the task index to delete: "))
        delete_task(task, index)
        print("Task deleted sucessfully.")
    elif choice == 5:
        
