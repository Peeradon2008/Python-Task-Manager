# show text to tell user and call feature.py
import feature as ft
from os import path
import exception as ex

data_length=len(ft.Accessjson().access()) #access json from feature.py

def showText(): #show text

    global data_length

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

def inputOption(option_selected): #choose option to create object from feature class
    
    match option_selected:
        case '1'|'2'|'3'|'5'|'6': #1) this option require taskname
            feature = ft.Feature(input("Task name : ")) #input taskname
            return feature
        
        case '4': #2) not require taskname
            feature = ft.Feature(None)
            return feature
        
        case '7'|"exit"|"Exit"|"EXIT": #3) exit
            return 7 #return 7 exit code
        
        case _: raise ex.OptionError(f"No > {option_selected} < option in this task manager")

def callFeature(option_selected,feature): #use task feature

    global data_length

    match option_selected,data_length:
        case '1',x if x>=0: 
            print("--------Add Task--------")
            feature.addtask()
        
        case '2',x if x>0: #2-6 can use only unblank json file
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

        case _: raise ex.OptionError(f"No > {option_selected} < option in this task manager")

#----------------------------------End Function---------------------------------------#