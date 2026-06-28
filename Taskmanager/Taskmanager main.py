import frontend as fr
import feature as ft
import exception as ex

while True: 
    try:
        print("---------Task Manager---------")

        data_length = len(ft.Accessjson().access())

        fr.showText(data_length)
        option_selected = input("Option Select (Number or Type Exit) : ")
        feature_option=fr.inputOption(option_selected)

        if feature_option==7: #7 is exitcode
            print("------------Exit Program------------")
            break
        else:
            fr.callFeature(option_selected,data_length,feature_option)

    except ex.OptionError as e:
        print("---------------------------------------")
        print(e)
        print("---------------------------------------")
    
    except ex.TaskNotFoundError as e:
        print(e)
        