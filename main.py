def main():
    my_tasks = []
    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter your task: ")
            my_tasks.append(task)
            print("Task added successfully!")

        elif choice == "2":
            if len(my_tasks) == 0:
                print("No tasks available.")
            else:
                print("\nYour Tasks:")
                for index, task in enumerate(my_tasks, start=1):
                    print(index, "-", task)

        elif choice == "3":
            print("Goodbye!")
            break        
        
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()