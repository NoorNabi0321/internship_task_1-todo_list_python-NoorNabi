import json

def main():
    try:
        with open("tasks.json", "r") as file:
            my_tasks = json.load(file)
    except:
        my_tasks = []
        
    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter your task: ")

            if task == "":
                print("Task cannot be empty!")
            else:
                my_tasks.append(task)

                # Save tasks
                with open("tasks.json", "w") as file:
                    json.dump(my_tasks, file)

                print("Task added successfully!")

        elif choice == "2":
            if len(my_tasks) == 0:
                print("No tasks available.")
            else:
                print("\nYour Tasks:")
                for i, task in enumerate(my_tasks, start=1):
                    print(i, "-", task)

        elif choice == "3":
            print("Goodbye!")
            break        
        
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()