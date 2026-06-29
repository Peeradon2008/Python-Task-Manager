import frontend as fr
import exception as ex

while True: 
    try:
        print("---------Task Manager---------")

        data_length = len(fr.getData()) #real time checking data_length

        fr.showText(data_length)
        option_selected = input("Option Select (Number or Type Exit) : ")
        exitcode=fr.callFeature(option_selected,data_length)

        if exitcode==True: #exitcode
            print("------------Exit Program------------")
            break #break loop

    except ex.OptionError as e:
        print("---------------------------------------")
        print(e)
        print("---------------------------------------")
    
    except ex.TaskNotFoundError as e:
        print(e)