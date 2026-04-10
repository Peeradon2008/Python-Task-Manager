import feature as ft
from json import load
from os import path
while True:
    try:    
        file_found=path.exists("D:/Github Repo/Python-Task-Manager/task.json")
        print("---------Task Manager---------")
        if file_found:
            print("""  -------Choose Option-------
1 Add Task
2 Delete Task
3 Show All Task
4 Commit Task
5 Edit Task
6 Exit""")
            with open("D:/Github Repo/Python-Task-Manager/task.json") as f:
                data = load(f)
        else:
            data=None
            print("""Choose Option
1 Add Task
or Type Exit""")
        choose=(input("Option Select (Number or Exit) : "))
        match choose,file_found:
            case '1',True|False:
                print("--------Add Task--------")
                ft.addtask(data,file_found)
            case '2',True: 
                print("--------Delete Task--------")
                ft.deletetask(data)
            case '3',True:
                print("--------Show All Task--------")
                ft.showtask(data)
            case '4',True:
                print("--------Commit Task--------")
                ft.taskcommit(data)
            case '5',True:
                print("--------Edit Task--------")
                ft.taskedit(data)
            case '6' | "Exit" | "exit",True|False:
                print("--------Exit--------")
                break
            case _:
                raise Exception

    except Exception:
        print("---------------------------------------")
        print("No that option in this task manager")
        print("---------------------------------------")