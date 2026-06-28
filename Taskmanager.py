import frontend as fr
import exception as ex

while True: 
    try:
        print("---------Task Manager---------")
        fr.showText()
        option_selected = input("Option Select (Number or Type Exit) : ")
        feature_option=fr.inputOption(option_selected)

        if feature_option==7: #7 is exitcode
            print("------------Exit Program------------")
            break
        else:
            fr.callFeature(option_selected,feature_option)

    except ex.OptionError as e:
        print("---------------------------------------")
        print(e)
        print("---------------------------------------")
    
    except ex.TaskNotFoundError as e:
        print(e)
        