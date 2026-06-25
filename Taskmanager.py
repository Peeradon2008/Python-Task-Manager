import frontend as fr
import exception as ex
while True: 
    try:
        print("---------Task Manager---------")
        exitcode=fr.main() #call frontend module
        # and return exit code to exit program (break loop)
        
        if exitcode==7:
            break

    except ex.OptionError as e:
        print("---------------------------------------")
        print(e)
        print("---------------------------------------")
    
    except ex.TaskNotFoundError as e:
        print(e)
        