print("\t\t\t-To do List App-\n")
task_list = []
print("\nMenu:")
print("1. Add Task")
print("2. View Tasks")
print("3. Remove Task")
print("4. Remove All Tasks")
print("5. Exit")
while True:
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue
    if choice == 1:
        task = input("Enter your Task: ")
        task_list.append(task)
        print("Task added.")
    elif choice == 2:
        if not task_list:
            print("No tasks yet!")
        else:
            print("Your Tasks:")
            for i, task in enumerate(task_list, start=1):
                print(f"{i}. {task}")
    elif choice == 3:
        if not task_list:
            print("No tasks to remove.")
            continue
        try:
            task_no = int(input("Enter the task number to remove: "))
            if 1 <= task_no <= len(task_list):
                removed_task = task_list.pop(task_no - 1)
                print(f"Removed: {removed_task}")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
    elif choice == 4:
        task_list.clear()
        print("All tasks removed.")
    elif choice == 5:
        print("Exiting To-Do List App. Goodbye!")
        break
    else:
        print("Invalid choice. Please select between 1 and 5.")
