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
4 Commit Task
5 Edit Task
6 Exit""")
        choose=(input("Option Select (Number or Type Exit) : "))
        match choose,len(data):
            case '1',x if x>=0:
                print("--------Add Task--------")
                feature = ft.Feature(input("Task name : "))
                feature.addtask()
            
            case '2',x if x>0: 
                print("--------Delete Task--------")
                feature = ft.Feature(input("Task name : "))
                feature.deletetask()
            
            case '3',x if x>0:
                print("--------Search Task--------")
                feature = ft.Feature(input("Task name : "))
                feature.searchtask()
            
            case '4',x if x>0:
                print("--------Commit Task--------")
                feature = ft.Feature(input("Task name : "))
                feature.taskcommit()
            
            case '5',x if x>0:
                print("--------Edit Task--------")
                feature = ft.Feature(input("Task name : "))
                feature.taskedit()
            
            case '6'|"exit"|"Exit"|"EXIT",x if x>=0:
                print("--------Exit--------")
                break
            
            case _,_:
                raise ex.OptionError(f"No > {choose} < option in this task manager")

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