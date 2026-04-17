import json
import exception as ex
json_file="D:/Github Repo/Python-Task-Manager/task.json"

class Feature:
    def __init__(self, task_name):
        with open(json_file) as f:
            self.__data = json.load(f)
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
        if len(self.__data) == 0:
            raise ex.TaskNotFoundError
        else:
            if self.__name in self.__data:
                del self.__data[self.__name]
                self.savetask()
                print("Task Deleted...\n")
            elif self.__name not in self.__data:
                raise ex.TaskDeleteError

    def taskcommit(self):
        if len(self.__data) == 0:
            raise ex.TaskNotFoundError
        else:
            if self.__name in self.__data:
                self.__data[self.__name].update({"completed":True})
                self.savetask()
                print("Task Commit...\n")
            elif self.__name not in self.__data:
                raise ex.TaskCommitError

    def searchtask(self):
        if len(self.__data) == 0:
            raise ex.TaskNotFoundError
        else:
            if self.__name in self.__data:
                searched = self.__data[self.__name]
                print(f"""----------------------------------------
name : {searched["name"]}
description : {searched["description"]}
completed : {searched["completed"]}
----------------------------------------""")
            elif self.__name not in self.__data:
                raise ex.TaskSearchError
            
    
    def taskedit(self):
        if len(self.__data) == 0:
            raise ex.TaskeditError
        else:
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
                raise ex.TaskNotFoundError
            
        

#----------------------------------End Class---------------------------------------#
