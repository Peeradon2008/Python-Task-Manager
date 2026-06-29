import json
import exception as ex
import os
json_file="task storage/task.json"

class Accessjson:
    def __init__(self): #check everytime if Json not exist to prevent bug
        if not os.path.exists(json_file):
            space={}
            with open(json_file,'x') as f:
                json.dump(space,f)
    
    def access(self): #import data from json file
        with open(json_file) as f:
            __data = json.load(f)
            return __data
class Feature(Accessjson): #have 6 feature
    def __init__(self,task_name):
        self.__data = super().access() #import json to temporary data
        self.__name = task_name
    
    def savetask (self): #export data to json
        with open(json_file,'w') as f:
            json.dump(self.__data,f,indent=2)

    def addtask(self): #1
        task={}
        task["name"]=self.__name    #setname
        task["description"]=input(f"{self.__name} description : ") #set description
        task["completed"]=False     #set default status
        self.__data.update({self.__name:task}) #update data
        self.savetask()             #export to json
        print("Task Added...\n")
    
    def deletetask(self): #2
        if self.__name in self.__data:  #search if that name is exist
            del self.__data[self.__name] #delete
            self.savetask()             #export to json
            print("Task Deleted...\n")

        elif self.__name not in self.__data:
            raise ex.TaskNotFoundError(f"""---------Delete Failed---------
Can't find task name {self.__name}""")

    def taskcommit(self): #3
        if self.__name in self.__data: #search if that name is exist
            self.__data[self.__name].update({"completed":True}) #set new status
            self.savetask() #export to json
            print("Task Commit...\n")
        elif self.__name not in self.__data:
            raise ex.TaskNotFoundError(f"""---------Commit Failed---------
Can't find task name {self.__name}""")
    
    def showalltask(self): #4
        for task in self.__data.values(): #Loop
            print(f"name : {task["name"]}")
            print(f"description : {task["description"]}")
            print(f"completed : {task["completed"]}")
            print("------------------------------------------")

    def searchtask(self): #5
        if self.__name in self.__data: #search if that name is exist
            searched = self.__data[self.__name]     #access temp data
            print("----------------------------------------")
            print(f"name : {searched["name"]}")
            print(f"description : {searched["description"]}")   #Loop
            print(f"completed : {searched["completed"]}")
            print("----------------------------------------")
        elif self.__name not in self.__data:
            raise ex.TaskNotFoundError(f"""---------Search Failed---------
Can't find task name {self.__name}""")
            
    
    def taskedit(self): #6
        if self.__name in self.__data: #search if that name is exist
            print("""option_selected what you want to edit
1 name
2 description
3 status""")
            edit=int(input("Edit Option : "))
            match edit:
                case 1:
                    new_name = input("new name : ")
                    self.__data[self.__name].update({"name":new_name}) #set new name
                    self.__data[new_name]=self.__data.pop(self.__name) #create new Json obj.
                    self.__name = new_name #new name update
                case 2:
                    new_des = input("new descriotion : ")
                    self.__data[self.__name].update({"description":new_des}) #set new description
                
                case 3:self.__data[self.__name].update({"completed":False}) #reset status
                case _:
                    raise ex.OptionError(f"No > {edit} < in this option")
            self.savetask()     #export to json
            print("Task Edited...\n")
        elif self.__name not in self.__data:
            raise ex.TaskNotFoundError(f"""---------Edit Failed---------
Can't find task name {self.__name}""")

#----------------------------------End Class---------------------------------------#
