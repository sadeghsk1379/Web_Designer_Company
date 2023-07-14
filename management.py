from person import Person
from department_employees import Department_Employees
class Management(Person,Department_Employees):
    Managements=[]
    def __init__(self,Section,**kwargs) -> None:
        self.Section=Section
        
        super.__init__(self,**kwargs)
