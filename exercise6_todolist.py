
class Task:
     def __init__(self, task_name, description, due_date, difficulty, iscompleted = False):
        self.task_name = task_name
        self.description = description
        self.due_date = due_date
        self.difficulty = difficulty
        self.iscompleted = iscompleted
        self.taskID = ''.join(random.choices(string.digits, k=6))

     def __str__(self):
        return (
            f"ID: {self.taskID} | "
            f"Name: {self.task_name} | "
            f"Description: {self.description} | "
            f"Due: {self.due_date} | "
            f"Difficulty: {self.difficulty} | "
            f"Completed: {self.iscompleted}"
        )

class TodoList:
    def __init__(self):
        self.list = []
        self.listID = ''.join(random.choices(string.digits, k=10))

    def delete_task(self, answer, taskID):
        if answer not in ("y","Y","n","N"):
            raise ValueError("Select (Y/N)")
        elif answer in ("Y","y"):
            for task in self.todoList.list:
                if task.taskID == taskID:
                    self.list.remove(task)
                    return
        else:
            print("What else would you like to do?")

    def add_task(self, task_name, description, due_date, difficulty):

        taskID = ''.join(random.choices(string.digits, k=6))
        # create Task object
        new_task = Task(
            task_name,
            description,
            due_date,
            difficulty,
            taskID
        )
        self.list.append(new_task)
        print(f"Task '{task_name}' added with ID {taskID}")

    def iscompleted(self, taskID):
        for task in self.list:
            if task.taskID == taskID:
                task.iscompleted = True
                return
        raise ValueError("There is no task with that ID. Please try again")
    
    def display_list(self):
        for task in self.list:
            print(task.task_name)


class TodoView:

    def show_menu(self):
        print("\n--- Your todo-list ---")
        print("\n--- What would you like to do? ---")
        print("1) View list")
        print("2) Add task to your list")
        print("3) Delete task from your list")
        print("4) Mark task as completed")
        print("0) Exit")
    
    def menu_choice(self):
        return input("Which option would you like to choose?")

    def show_list(self, todo_list):
        if not todo_list.list:
            print("Your todo list is empty.")
            return
        for task in todo_list.list:
            print(task)

    def get_new_task_data(self):
        task_name = input("Task name: ")
        description = input("Description: ")
        while True:
            due_date = input("Due date (Format: DD.MM.YYYY): ")
            try:
                datetime.strptime(due_date, "%d.%m.%Y")
                break
            except ValueError:
                print("Invalid format. Please use DD.MM.YYYY")
        print("Please enter a number between 1 and 6")
        
        while True:
            difficulty = int(input("Difficulty (1–6): "))
            if 1 <= difficulty <= 6:
                break
        print("Please enter a number between 1 and 6")
        return task_name, description, due_date, difficulty

    def ask_task_id(self):
        return input("Enter task ID: ")
    
    def confirm_delete(self):
        return input("Are you sure you want to delete this task? (y/n): ")
    
    def confirm_completion(self, task_id):
        return input(f"Are you sure you want to mark the task with the ID {task_id} as completed? (y/n): ")
    

class TodoController:
    def __init__(self, todo_list, view):
        self.todo_list = todo_list
        self.view = view#

    def run(self):
        while True:
            self.view.show_menu()
            choice = self.view.menu_choice()

            if choice == "1":
                self.view.show_list(self.todo_list)

            elif choice == "2":
                self.add_task_flow()

            elif choice == "3":
                self.remove_task_flow()

            elif choice == "4":
                self.completed_task_flow()

            elif choice == "0":
                break

            else:
                print("Invalid choice")   
    
    def add_task_flow(self):
        name, desc, due, diff = self.view.get_new_task_data()
        self.todo_list.add_task(name, desc, due, diff)

    def remove_task_flow(self):
        task_id = self.view.ask_task_id()
        confirm = self.view.confirm_delete()

        if confirm not in ["Y","y"]:
            return
        for task in self.todo_list.list:
            if task.taskID == task_id:
                self.todo_list.list.remove(task)
                print("Task deleted")
                return
        print("Task not found.")

    def completed_task_flow(self):
        task_id = self.view.ask_task_id()
        completed = self.view.confirm_completion()

        if completed in ["Y","y"]:
            for task in self.todo_list.list:
                if task.taskID == task_id:
                    task.iscompleted = True
                    print("The task was marked as completed")
                    return
            print("Task not found")


def main():
    todo_list = TodoList()
    view = TodoView()
    controller = TodoController(todo_list, view)
    controller.run()


if __name__ == "__main__":
 
    from datetime import datetime
    import random
    import string

    main()