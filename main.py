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

        elif choice == "3":
            print("Goodbye!")
            break        


if __name__ == "__main__":
    main()