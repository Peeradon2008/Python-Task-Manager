import json
from os import path


def addtask():
    task={}
    
    #ใส่ข้อมูล task ที่จะเพิ่ม ใน dict
    task_name=input("Task Name : ")
    task_des =input(f"{task_name} Description : ")
    task["name"]=task_name          #task.update({"name":task_name})
    task["description"]=task_des    #task.update({"description":task_des})
    task["completed"]=False            #task.update({"completed":False})
    print("Task Added...\n")

    if not path.exists("D:/Github Repo/Python-Task-Manager/task.json"):   #กรณี file ยังไม่เคยถูกสร้าง (ไม่เคยใช้)
        user={}
        user.update({task_name:task})           #<-- เอา task เพิ่มเข้าไปใน list/array
        with open("D:/Github Repo/Python-Task-Manager/task.json",'a') as f:
            json.dump(user,f,indent=2)          #<-- แปลงและเก็บข้อมูลให้เป็น Json object+array
            """ข้อมูลถูกเก็บใน Json file แล้ว"""
    
    else: #กรณีที่ file ถูกสร้างแล้ว (เคยใช้)
        with open("D:/Github Repo/Python-Task-Manager/task.json") as f:
            data=json.load(f)       #<-- ดึงข้อมูลใน Json มาเก็บไว้ใน Data
        data.update({task_name:task})     #update ข้อมูลใหม่ใน list Data

        with open ("D:/Github Repo/Python-Task-Manager/task.json",'w') as f:
            json.dump(data,f,indent=2) 
            """Rewrite Json file ด้วยข้อมูลที่ update แล้ว"""

"""--------------------------------------------------------------------------------------------------"""
def deletetask():   
    try:    
        with open("D:/Github Repo/Python-Task-Manager/task.json") as f:
            data=json.load(f)
        task_name=input("Task name : ")
        if task_name in data:
            del data[task_name]
            with open("D:/Github Repo/Python-Task-Manager/task.json",'w') as f:
                json.dump(data,f,indent=2)
            print("Task Deleted...\n")
        else:
            raise Exception("Error :Task Name Not Found")
    except Exception:
        print("---------------------------------------")
        print(f"""Can't Delete Task
Name:"{task_name}" Not Exist""")
        print("---------------------------------------")


"""--------------------------------------------------------------------------------------------------"""
def showtask():
    count=0

    with open("D:/Github Repo/Python-Task-Manager/task.json") as f:
        data=json.load(f)   #<-- ดึงข้อมูลใน Json มาเก็บไว้ใน Data
    
    for task in data.values(): #show ข้อมูล ทั้งหมด
        count+=1
        print(f"No. {count}")
        print(f"""name: {task["name"]}
description: {task["description"]}
completed: {task["completed"]}""")
        print('--------------------------------------------------')
    count=0 

"""--------------------------------------------------------------------------------------------------"""
def taskcommit():
    try:    
        with open("D:/Github Repo/Python-Task-Manager/task.json") as f:
            data=json.load(f)   #<-- ดึงข้อมูลใน Json มาเก็บไว้ใน Data
        task_name=input("Task name : ")
        if task_name in data:
            data[task_name].update({"completed":True})
            with open("D:/Github Repo/Python-Task-Manager/task.json",'w') as f:
                json.dump(data,f,indent=2)
            print("Task Commit...\n")

        else:
            raise Exception("Error : Task Not Found")

    except Exception:
        print("---------------------------------------")
        print(f"""Can't Commit Task
Name:"{task_name}" Not Exist""")
        print("---------------------------------------")