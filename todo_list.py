#Todo List Application [junior Software engineer understandable]
tasks = [] #initialize empty list to store a Task  

#function to display the menu
def show_menu():  
    print("\n---Todo List Menu---") 
    print("1. View Tasks")
    print("2. Add a Task")
    print("3. Mark a Task as completed")
    print("4. Delete a Task")
    print("5. Exit")

#function to view all tasks
def view_tasks():
    if not tasks:
        print("No Task found!")
    else:
        print("\n---Your Tasks---")
        for index, task in enumerate(tasks, start=1):
            status = "Done" if task["completed"] else "Not done"
            print(f"{index}. {task['name']} - {status}")

#function to add a task
def add_task():
    task_name = input("Enter your task name:")
    tasks.append({"name" : task_name, "completed" : False})
    print(f"Task '{task_name}' added successfully!")

#function to mark a task as completed
def mark_completed():
    view_tasks()
    try:
        task_number = int(input("Enter the task number to mark as completed:"))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["completed"] = True
            print(f"Task '{tasks[task_number - 1]['name']}' mark as completed!")
        else:
            print("Invalid Task number!")
    except ValueError:
        print("Please enter a Valid number  ")

#function to delete a task
def delete_tasks():
    view_tasks()
    try:
        task_number = int(input("Enter the task number to delete: "))
        if 1 <= task_number <=len(tasks):
            deleted_task = tasks.pop(task_number - 1)
            print(f"Task '{deleted_task['name']}' deleted successfully!")
        else:
            print("Invalid Task number!")
    except ValueError:
        print("Please enter a valid number")

    #main program loop
def main():
        while True:
            show_menu()
            choice = input("Enter your choice [1-5]: ")
            if choice == "1":
                view_tasks()
            
            elif choice == "2":
                add_task()
             
            elif choice == "3":
                mark_completed()
            
            elif choice == "4":
                delete_tasks()
            
            elif choice == "5":
                print("Existing the application. GoodBye!")
                break
            else:
                print("Invalid choice! Please try again.")

#run the program
if __name__ == "__main__":
    main()
            
            
        
