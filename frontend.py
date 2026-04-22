import feature as ft
from exception import OptionError
class Frontend:
    def main(self):
        self.__length=len(ft.Data().access())
        self.text()
        self.__choose = input("Option Select (Number or Type Exit) : ")
        x=self.input()
        if x == 7:
            return x
        else:
            self.callfeature()

    def text(self):
        match self.__length:
            case 0:
                print("""  -------Choose Option-------
1 Add Task
-Exit""")
            case x if x>0 :
                print("""  -------Choose Option-------
1 Add Task
2 Delete Task
3 Search Task
4 Show All Task
5 Commit Task
6 Edit Task
7 Exit""")

    def input(self):
        match self.__choose:
            case '1'|'2'|'3'|'5'|'6': self.feature = ft.Feature(input("Task name : "))
            case '4':self.feature = ft.Feature("")
            case '7'|"exit"|"Exit"|"EXIT":
                return 7
            case _: raise OptionError(f"No > {self.__choose} < option in this task manager")
    
    def callfeature(self):
        match self.__choose,self.__length:
            case '1',x if x>=0:
                print("--------Add Task--------")
                self.feature.addtask()
            
            case '2',x if x>0: 
                print("--------Delete Task--------")
                self.feature.deletetask()
            
            case '3',x if x>0:
                print("--------Search Task--------")
                self.feature.searchtask()
            case '4',x if x>0:
                print("--------Show All Task--------")
                self.feature.showalltask()
            case '5',x if x>0:
                print("--------Commit Task--------")
                self.feature.taskcommit()
            
            case '6',x if x>0:
                print("--------Edit Task--------")
                self.feature.taskedit()

