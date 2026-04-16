import json
import exception as ex
json_file="D:/Github Repo/Python-Task-Manager/task.json"
class Addtask:
    def __init__(self,data:dict,found:bool):
        self.__name = input("Task name : ")
        self.__data = data
        self.__task = self.__input() 
        if found:
            self.__found()
        else:
            self.__notfound()
    
    def __input(self):
        task={}
        task_des = input(f"{self.__name} Description : ")
        task["name"]=self.__name  #task.updated({"name":task_name})
        task["description"]=task_des #task.updated({"description":task_des})
        task["completed"]=False  #task.updated({"completed":False})
        return task
    
    def __found(self):
        self.__data.update({self.__name:self.__task})
        self.writejsonfile()
    
    def __notfound(self):
        user={}
        user.update({self.__name:self.__task})
        with open(json_file,'a') as f:
            json.dump(user,f,indent=2)
    
    def writejsonfile(self):
        with open(json_file,'w') as f:
            json.dump(self.__data,f,indent=2)

class Deletetask(Addtask):
    def __init__(self,data:dict):
        self.__data = data
        self.__name = input("Task name : ")
        if self.__name in self.__data:
            self.__delete
        else:
            raise ex.TaskNotFoundError
    def __delete(self):
        del self.__data[self.__name]
    def writejsonfile(self):
        super().writejsonfile()