import feature as ft
while True:
    try:    
        print("Task Manager")
        print("""1 Add Task
2 Delete Task
3 Show All Task
4 Commit Task
5 Exit""")
        choose=int(input("Option Select (1,2,3,4,5) : "))
        match choose:
            case 1:
                print("--------Add Task--------")
                ft.addtask()
            case 2:
                print("--------Delete Task--------")
                ft.deletetask()
            case 3:
                print("--------Show All Task--------")
                ft.showtask()
            case 4:
                print("--------Commit Task--------")
                ft.taskcommit()
            case 5:
                print("--------Exit--------")
                break

    except ValueError:
        print("---------------------------------------")
        print("No that option in this task manager")
        print("---------------------------------------")