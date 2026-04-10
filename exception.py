class OptionError(Exception):
    pass
class TaskNotFoundError(Exception):
    pass
class filePath:
    def __init__(self):
        self._filepath = "D:/Github Repo/Python-Task-Manager/task.json"
    def filepathchange(self,new_path):
        self._filepath = new_path
    def showpath(self):
        print(f"Your File path -> {self._filepath}")