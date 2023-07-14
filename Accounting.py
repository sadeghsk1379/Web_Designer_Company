from person import Person
from department_employees import Department_Employees
class Accounting(Person,Department_Employees):
    Accounting=[]
    def __init__(self,Department_Section,Costs_Of_Section,Income_Of_Section,Hesabdaris,**kwargs) -> None:
        self.Department_Section=Department_Section
        self.Costs_Of_Section=Costs_Of_Section
        self.Income_Of_Section=Income_Of_Section
        
        super().__init__(self,**kwargs)
        Accounting.append(self)
        
