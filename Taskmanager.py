import feature as ft
import exception as ex
while True: 
    try:
        data=ft.Data().access()
        print("---------Task Manager---------")
        match len(data):
            case 0:
                print("""  -------Choose Option-------
1 Add Task
-Exit""")
            case x if x>0 :
                print("""  -------Choose Option-------
1 Add Task
2 Delete Task
3 Search Task
4 Show All Task
5 Commit Task
6 Edit Task
7 Exit""")
        choose=(input("Option Select (Number or Type Exit) : "))
        match choose:
            case '1'|'2'|'3'|'5'|'6': feature = ft.Feature(input("Task name : "))
            case '4':feature = ft.Feature("")
            case '7'|"exit"|"Exit"|"EXIT": break
            case _,_: raise ex.OptionError(f"No > {choose} < option in this task manager")
        match choose,len(data):
            case '1',x if x>=0:
                print("--------Add Task--------")
                feature.addtask()
            
            case '2',x if x>0: 
                print("--------Delete Task--------")
                feature.deletetask()
            
            case '3',x if x>0:
                print("--------Search Task--------")
                feature.searchtask()
            case '4',x if x>0:
                print("--------Show All Task--------")
                feature.showalltask()
            case '5',x if x>0:
                print("--------Commit Task--------")
                feature.taskcommit()
            
            case '6',x if x>0:
                print("--------Edit Task--------")
                feature.taskedit()

    except ex.OptionError as e:
        print("---------------------------------------")
        print(e)
        print("---------------------------------------")
    except ex.TaskNotFoundError as e:
        print("---------------------------------------")
        print(e)
        print("---------------------------------------")
    except ex.TaskDeleteError as e:
        print("---------------------------------------")
        print(e)
        print("---------------------------------------")
    except ex.TaskSearchError as e:
        print("---------------------------------------")
        print(e)
        print("---------------------------------------")
    except ex.TaskCommitError as e:
        print("---------------------------------------")
        print(e)
        print("---------------------------------------")
    except ex.TaskeditError as e:
        print("---------------------------------------")
        print(e)
        print("---------------------------------------")