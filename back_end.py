from person import Person
from department_employees import Department_Employees
class Back_end(Person,Department_Employees):
    Back_ends=[]
    def __init__(self,Language,Number_Of_Projects,Cost_of_Project,Back_ends,**kwargs) -> None:
        self.Language=Language
        self.Number_Of_Projects=Number_Of_Projects
        self.Cost_of_Project=Cost_of_Project
        
        
        super().__init__(self,**kwargs)
        Back_ends .append(self)
