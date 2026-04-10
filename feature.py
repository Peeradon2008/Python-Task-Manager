import json
import exception as ex

def addtask(data,found):
    task={}
    #ใส่ข้อมูล task ที่จะเพิ่ม ใน dict
    task_name=input("Task Name : ")
    task_des =input(f"{task_name} Description : ")
    task["name"]=task_name          #task.update({"name":task_name})
    task["description"]=task_des    #task.update({"description":task_des})
    task["completed"]=False            #task.update({"completed":False})
    print("Task Added...\n")

    if found:   #กรณีที่ file ถูกสร้างแล้ว (เคยใช้)
        data.update({task_name:task})     #update ข้อมูลใหม่ใน list Data

        with open ("D:/Github Repo/Python-Task-Manager/task.json",'w') as f:
            json.dump(data,f,indent=2) 
            """Rewrite Json file ด้วยข้อมูลที่ update แล้ว"""
    else: #กรณี file ยังไม่เคยถูกสร้าง (ไม่เคยใช้)
        user={}
        user.update({task_name:task})           #<-- เอา task เพิ่มเข้าไปใน list/array
        with open("D:/Github Repo/Python-Task-Manager/task.json",'a') as f:
            json.dump(user,f,indent=2)          #<-- แปลงและเก็บข้อมูลให้เป็น Json object+array
            """ข้อมูลถูกเก็บใน Json file แล้ว"""

"""--------------------------------------------------------------------------------------------------"""
def deletetask(data):   
    try:    
        task_name=input("Task name : ")
        if task_name in data:
            del data[task_name]
            with open("D:/Github Repo/Python-Task-Manager/task.json",'w') as f:
                json.dump(data,f,indent=2)
            print("Task Deleted...\n")
        else:
            raise ex.TaskNotFoundError("Error :Task Not Found")
    except ex.TaskNotFoundError:
        print("---------------------------------------")
        print(f"""Can't Delete Task
Name:"{task_name}" Not Exist""")
        print("---------------------------------------")


"""--------------------------------------------------------------------------------------------------"""
def showtask(data):
    count=0
    
    for task in data.values(): #show ข้อมูล ทั้งหมด
        count+=1
        print(f"No. {count}")
        print(f"""name: {task["name"]}
description: {task["description"]}
completed: {task["completed"]}""")
        print('--------------------------------------------------')
    count=0 

"""--------------------------------------------------------------------------------------------------"""
def taskcommit(data):
    try:    
        task_name=input("Task name : ")
        if task_name in data:
            data[task_name].update({"completed":True})
            with open("D:/Github Repo/Python-Task-Manager/task.json",'w') as f:
                json.dump(data,f,indent=2)
            print("Task Commit...\n")

        else:
            raise ex.TaskNotFoundError("Error : Task Not Found")

    except ex.TaskNotFoundError:
        print("---------------------------------------")
        print(f"""Can't Commit Task
Name:"{task_name}" Not Exist""")
        print("---------------------------------------")

def taskedit(data):
    try:    
        task_name=input("Task name : ")
        if task_name in data:
            print("""Choose what you want to edit
    1 name
    2 description
    3 completed status""")
            edit=int(input("Edit Option : "))
            match edit:
                case 1:
                    new_name = input("New Name : ")
                    data[task_name].update({"name":new_name})
                    data[new_name]=data.pop(task_name)
                    print(f"Name updated to {data[new_name]["name"]}")
                case 2:
                    new_des = input("New Description : ")
                    data[task_name].update({"description":new_des})
                    print(f"Description updated to {data[task_name]["description"]}")
                case 3:
                    data[task_name].update({"completed":False})
                    print(f"Complete Status updated to {data[task_name]["completed"]}")
            with open("D:/Github Repo/Python-Task-Manager/task.json",'w') as f:
                    json.dump(data,f,indent=2)
        else:
            raise ex.TaskNotFoundError("Error : Task Not Found")
    except ex.TaskNotFoundError:
        print("---------------------------------------")
        print(f"""Can't Edit Task
Name:"{task_name}" Not Exist""")
        print("---------------------------------------")
