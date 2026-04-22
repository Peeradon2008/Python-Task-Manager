import frontend as fr
import exception as ex
while True: 
    try:
        print("---------Task Manager---------")
        Taskmanager=fr.Frontend().main()
        if Taskmanager==7:
            break
            #Goal
            #Test no file situation
            #Test Error
    except ex.OptionError as e:
        print("---------------------------------------")
        print(e)
        print("---------------------------------------")
    
    except ex.TaskNotFoundError as e:
        print(e)
        