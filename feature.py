import json
from os import path
task={}
def addtask():
    task_name=input("Task Name : ")
    task_des =input(f"{task_name} Description :")
    task["name"]=task_name
    task["description"]=task_des
    task["status"]=False
    if not path.exists("D:/Github Repo/Python-Task-Manager/task.json"):
        user=[]
        user.append(task)
        with open("D:/Github Repo/Python-Task-Manager/task.json",'a') as f:
            json.dump(user,f,indent=2)
    else:
        with open("D:/Github Repo/Python-Task-Manager/task.json") as f:
            data=json.load(f)
        data.append(task)
        print(data)
        with open ("D:/Github Repo/Python-Task-Manager/task.json",'w') as f:
            json.dump(data,f,indent=2)

def deletetask():
    pass

def showtask():
    with open("D:/Github Repo/Python-Task-Manager/task.json") as f:
        data=json.load(f)
        for task in data:
            print(f"""name: {task["name"]}
description: {task["description"]}
status: {task["status"]}""")
            print('--------------------------------------------------')
                 

def taskcommit():
    pass