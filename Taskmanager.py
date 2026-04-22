import frontend as fr
import exception as ex
while True: 
    try:
        print("---------Task Manager---------")
        Taskmanager=fr.Frontend().main()
        if Taskmanager==7:
            break

    except ex.OptionError as e:
        print("---------------------------------------")
        print(e)
        print("---------------------------------------")
    
    except ex.TaskNotFoundError as e:
        print(e)
    
    except ex.TaskDeleteError as e:
        print(e)
    
    
    except ex.TaskSearchError as e:
        print(e)
    
    except ex.TaskCommitError as e:
        print(e)
    
    except ex.TaskeditError as e:
        print(e)
        