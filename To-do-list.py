import sys

# A class representing a task
class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Done" if self.completed else "Pending"
        return f"{self.description} - [{status}]"


# A class representing the To-Do list
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        print(f"Task '{description}' added.")

    def update_task(self, index, description):
        if 0 <= index < len(self.tasks):
            self.tasks[index].description = description
            print(f"Task {index + 1} updated to '{description}'.")
        else:
            print(f"No task found at index {index + 1}.")

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
            print(f"Task {index + 1} marked as completed.")
        else:
            print(f"No task found at index {index + 1}.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            print(f"Task '{removed_task.description}' deleted.")
        else:
            print(f"No task found at index {index + 1}.")

    def show_tasks(self):
        if not self.tasks:
            print("Your to-do list is empty!")
        else:
            print("\nTo-Do List:")
            for idx, task in enumerate(self.tasks, 1):
                print(f"{idx}. {task}")


def display_menu():
    print("\nTo-Do List Application")
    print("1. Add task")
    print("2. Update task")
    print("3. Mark task as completed")
    print("4. Delete task")
    print("5. Show tasks")
    print("6. Exit")


def main():
    to_do_list = ToDoList()

    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            description = input("Enter task description: ").strip()
            to_do_list.add_task(description)
        elif choice == '2':
            to_do_list.show_tasks()
            index = int(input("Enter task number to update: ")) - 1
            description = input("Enter new task description: ").strip()
            to_do_list.update_task(index, description)
        elif choice == '3':
            to_do_list.show_tasks()
            index = int(input("Enter task number to mark as completed: ")) - 1
            to_do_list.mark_task_completed(index)
        elif choice == '4':
            to_do_list.show_tasks()
            index = int(input("Enter task number to delete: ")) - 1
            to_do_list.delete_task(index)
        elif choice == '5':
            to_do_list.show_tasks()
        elif choice == '6':
            print("Exiting the application. Have a productive day!")
            sys.exit()
        else:
            print("Invalid choice. Please select a valid option (1-6).")


if __name__ == "__main__":
    main()
