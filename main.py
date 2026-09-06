tasks = []

while True:
    print("\n===== MY TO-DO APP =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("✅ Task added!")

    elif choice == "2":
        if not tasks:
            print("No tasks yet.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

    elif choice == "3":
        if not tasks:
            print("No tasks to delete.")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

            number = int(input("Enter task number: "))

            if 1 <= number <= len(tasks):
                removed = tasks.pop(number - 1)
                print(f"🗑️ Deleted: {removed}")
            else:
                print("❌ Invalid number.")

    elif choice == "4":
        print("Goodbye! 👋")
        break

    else:
        print("❌ Invalid choice.")
