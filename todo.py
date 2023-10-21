to_do_list = {}

while True:
    print("\nChoose your Option:")
    print("1. Add a task")
    print("2. Display tasks")
    print("3. Remove a task")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter a new task for today: ")
        to_do_list[len(to_do_list) + 1] = task
        print(f"Task '{task}' has been added successfully to your to-do list!")
    elif choice == "2":
        if to_do_list:
            print("\nYour to-do list:")
            for i, task in to_do_list.items():
                print(f"{i}. {task}")
        else:
            print("\nYour to-do list is empty.")
    elif choice == "3":
        if to_do_list:
            print("\nYour to-do list for today:")
            for i, task in to_do_list.items():
                print(f"{i}. {task}")
            try:
                task_number = int(input("Enter the number of the task you want to remove: "))
                if task_number in to_do_list:
                    removed_task = to_do_list.pop(task_number)
                    print(f"Task '{removed_task}' has been removed from your to-do list.")
                else:
                    print("Invalid task number. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        else:
            print("Your to-do list is empty.")
    elif choice == "4":
        print("Happy Workinggg!")
        break
    else:
        print("Invalid choice. Please try again.")
