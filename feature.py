import json
import exception as ex
json_file="D:/Github Repo/Python-Task-Manager/task.json"
class Data:
    def access(self):
        with open(json_file) as f:
            self.__data = json.load(f)
            return self.__data
class Feature(Data):
    def __init__(self, task_name):
        self.__data = super().access()
        self.__name = task_name
    
    def savetask (self):
        with open(json_file,'w') as f:
            json.dump(self.__data,f,indent=2)

    def addtask(self):
        task={}
        task["name"]=self.__name
        task["description"]=input(f"{self.__name} description : ")
        task["completed"]=False
        self.__data.update({self.__name:task})
        self.savetask()
        print("Task Added...\n")
    
    def deletetask(self):
        if self.__name in self.__data:
            del self.__data[self.__name]
            self.savetask()
            print("Task Deleted...\n")
        elif self.__name not in self.__data:
            raise ex.TaskDeleteError(f"""---------Delete Failed---------
Can't find task name {self.__name}""")

    def taskcommit(self):
        if self.__name in self.__data:
            self.__data[self.__name].update({"completed":True})
            self.savetask()
            print("Task Commit...\n")
        elif self.__name not in self.__data:
            raise ex.TaskCommitError(f"""---------Commit Failed---------
Can't find task name {self.__name}""")
    
    def showalltask(self):
        for task in self.__data.values():
            print(f"name : {task["name"]}")
            print(f"description : {task["description"]}")
            print(f"completed : {task["completed"]}")
            print("------------------------------------------")

    def searchtask(self):
        if self.__name in self.__data:
            searched = self.__data[self.__name]
            print(f"----------------------------------------")
            print(f"name : {searched["name"]}")
            print(f"description : {searched["description"]}")
            print(f"completed : {searched["completed"]}")
            print("----------------------------------------")
        elif self.__name not in self.__data:
            raise ex.TaskSearchError(f"""---------Search Failed---------
Can't find task name {self.__name}""")
            
    
    def taskedit(self):
        if self.__name in self.__data:
            print("""Choose what you want to edit
1 name
2 description
3 status""")
            edit=int(input("Edit Option : "))
            match edit:
                case 1:
                    new_name = input("new name : ")
                    self.__data[self.__name].update({"name":new_name})
                    self.__data[new_name]=self.__data.pop(self.__name)
                    self.__name = new_name
                case 2:
                    new_des = input("new descriotion : ")
                    self.__data[self.__name].update({"description":new_des})
                
                case 3:self.__data[self.__name].update({"completed":False})
            self.savetask()
            print("Task Edited...\n")
        elif self.__name not in self.__data:
            raise ex.TaskNotFoundError(f"""---------Edit Failed---------
Can't find task name {self.__name}""")
            
        

#----------------------------------End Class---------------------------------------#
