def to_do_list():
    tasks=[]
    while True:
        print("1.Add task")
        print("2.Remove task")
        print("3.Show task")
        print("4.Quit")
        choice =input("Enter your choice:")

        if choice=="1":
            task=input("Enter Task: ")
            tasks.append(task)
        elif choice=="2":
            task=input("Enter the Task to Remove: ")
            if task in tasks:
                tasks.remove(task)
            else:
                print("task Not Found!")
        elif choice=="3":
            print("Tasks: ")
            for task in tasks:
                print("- " + task)
        elif choice == "4":
            break
        else:
            print("Invalid choice!")
to_do_list()