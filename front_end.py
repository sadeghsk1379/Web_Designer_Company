from person import Person
from department_employees import Department_Employees
class Front_end(Person,Department_Employees):
    front_ends=[]
    def __init__(self,Number_Of_Projects,front_ends,**kwargs) -> None:
        
        self.Number_Of_Projects=Number_Of_Projects
        
        
        
        super().__init__(self,**kwargs)
        front_ends .append(self)
