#TO-DO-List

import os



#Function to load tasks from the file
def load_tasks(Todolist):
    tasks = [] #Initializes an empty list to store tasks.
    if os.path.exists(Todolist):
        with open(Todolist,'r')as file:
            tasks = file.readlines()
    return[task.strip() for task in tasks]#Returns the list of tasks, removing any extra whitespace or newline characters from each task.


#Function to Save Tasks

def save_tasks(Todolist, tasks):
    with open(Todolist,'w') as file:
        for task in tasks:#Loops through each task in the tasks list
            file.write(task + '\n') #Writes each task to the file, adding a newline character (\n) at the end.


#Function to Add task

def add_task(tasks):
    task= input("Enter the task you want to add: ")
    tasks.append(task)
    print(f"Task '{task}' added successfully.")



#Function to delete task

def delete_task(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter the task number to delete: "))
    if 0<task_num<= len(tasks):#Checks if the entered task number is valid
        removed_task = tasks.pop(task_num -1)#Removes the task (adjusting for 0-based indexing) and saves it in removed_task.
        print(f"Task'{removed_task}' deleted successfully.")
    else:
        print("Invalid task number!")


#Function to view task

def view_tasks(tasks):
    if not tasks:#Checks if the tasks list is empty
        print("No Tasks to display.")
    else:
        print("\nTo-Do List: ")
        for idx, task in enumerate(tasks,start =1):#Loops through the tasks, displaying each with a 1-based index.
            print(f"{idx}. {task}")


#MAIN FUNCTION


def main():
    filename = "tasks.txt"
    tasks = load_tasks(filename)

    while True:
        print("\nTo-Do List Application")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            save_tasks(filename, tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":#Ensures the main function runs only when the script is executed directly, not when imported.
    main()






