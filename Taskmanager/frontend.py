# show text to tell user and call feature.py
import feature as ft
import exception as ex

def getData ():
    data=ft.Accessjson().access()
    return data

def showText(data_length): #show text

    # only use Addtask unless task data have stored
    match data_length:
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
            
def callFeature(option_selected,data_length): #use task feature

    match option_selected,data_length:
        case '1',x if x>=0: 
            print("--------Add Task--------")
            ft.Feature(input("Task name : ")).addtask()
            exitcode=False
            return exitcode
        
        case '2',x if x>0: #2-6 can use only unblank json file
            print("--------Delete Task--------")
            ft.Feature(input("Task name : ")).deletetask()
            exitcode=False
            return exitcode
        
        case '3',x if x>0:
            print("--------Search Task--------")
            ft.Feature(input("Task name : ")).searchtask()
            exitcode=False
            return exitcode

        case '4',x if x>0:
            print("--------Show All Task--------")
            ft.Feature("").showalltask()
            exitcode=False
            return exitcode
        
        case '5',x if x>0:
            print("--------Commit Task--------")
            ft.Feature(input("Task name : ")).taskcommit()
            exitcode=False
            return exitcode
        
        case '6',x if x>0:
            print("--------Edit Task--------")
            ft.Feature(input("Task name : ")).taskedit()
            exitcode=False
            return exitcode
        
        case '7'|"exit"|"Exit"|"EXIT",x if x>=0:
            exitcode=True
            return exitcode #return exitcode True -> break loop

        case _: raise ex.OptionError(f"No > {option_selected} < option in this task manager")


#----------------------------------End Function---------------------------------------#