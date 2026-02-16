from datetime import datetime
import random
import string


class Task:
    def __init__(
        self,
        task_name: str,
        description: str,
        due_date: str,
        difficulty: int,
        iscompleted: bool = False
    ) -> None:
        self.task_name: str = task_name
        self.description: str = description
        self.due_date: str = due_date
        self.difficulty: int = difficulty
        self.iscompleted: bool = iscompleted
        self.taskID: str = ''.join(random.choices(string.digits, k=6))

    def __str__(self) -> str:
        return (
            f"ID: {self.taskID} | "
            f"Name: {self.task_name} | "
            f"Description: {self.description} | "
            f"Due: {self.due_date} | "
            f"Difficulty: {self.difficulty} | "
            f"Completed: {self.iscompleted}"
        )


class TodoList:
    def __init__(self) -> None:
        self.list: list[Task] = []
        self.listID: str = ''.join(random.choices(string.digits, k=10))

    def delete_task(self, answer: str, taskID: str) -> None:
        if answer not in ("y", "Y", "n", "N"):
            raise ValueError("Select (Y/N)")
        elif answer in ("Y", "y"):
            for task in self.list:
                if task.taskID == taskID:
                    self.list.remove(task)
                    return
        else:
            print("What else would you like to do?")

    def add_task(self, task_name: str, description: str, due_date: str, difficulty: int) -> None:
        # create Task object (Task generates its own ID)
        new_task = Task(
            task_name,
            description,
            due_date,
            difficulty
        )
        self.list.append(new_task)
        print(f"Task '{task_name}' added with ID {new_task.taskID}")

    def iscompleted(self, taskID: str) -> None:
        for task in self.list:
            if task.taskID == taskID:
                task.iscompleted = True
                return
        raise ValueError("There is no task with that ID. Please try again")
    
    def display_list(self) -> None:
        for task in self.list:
            print(task.task_name)


class TodoView:

    def show_menu(self) -> None:
        print("\n--- Your todo-list ---")
        print("\n--- What would you like to do? ---")
        print("1) View list")
        print("2) Add task to your list")
        print("3) Delete task from your list")
        print("4) Mark task as completed")
        print("0) Exit")
    
    def menu_choice(self) -> str:
        return input("Which option would you like to choose?")

    def show_list(self, todo_list: TodoList) -> None:
        if not todo_list.list:
            print("Your todo list is empty.")
            return
        for task in todo_list.list:
            print(task)

    def get_new_task_data(self) -> tuple[str, str, str, int]:
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

    def ask_task_id(self) -> str:
        return input("Enter task ID: ")
    
    def confirm_delete(self) -> str:
        return input("Are you sure you want to delete this task? (y/n): ")
    
    def confirm_completion(self, task_id: str) -> str:
        return input(f"Are you sure you want to mark the task with the ID {task_id} as completed? (y/n): ")
    

class TodoController:
    def __init__(self, todo_list: TodoList, view: TodoView) -> None:
        self.todo_list: TodoList = todo_list
        self.view: TodoView = view

    def run(self) -> None:
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
    
    def add_task_flow(self) -> None:
        name, desc, due, diff = self.view.get_new_task_data()
        self.todo_list.add_task(name, desc, due, diff)

    def remove_task_flow(self) -> None:
        task_id = self.view.ask_task_id()
        confirm = self.view.confirm_delete()

        if confirm not in ["Y", "y"]:
            return
        for task in self.todo_list.list:
            if task.taskID == task_id:
                self.todo_list.list.remove(task)
                print("Task deleted")
                return
        print("Task not found.")

    def completed_task_flow(self) -> None:
        task_id = self.view.ask_task_id()
        completed = self.view.confirm_completion(task_id)

        if completed in ["Y", "y"]:
            for task in self.todo_list.list:
                if task.taskID == task_id:
                    task.iscompleted = True
                    print("The task was marked as completed")
                    return
            print("Task not found")


def main() -> None:
    todo_list = TodoList()
    view = TodoView()
    controller = TodoController(todo_list, view)
    controller.run()


if __name__ == "__main__":
    
    main()