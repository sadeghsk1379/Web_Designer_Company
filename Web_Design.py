from person import Person
from department_employees import Department_Employees
class web_design(Person,Department_Employees):
    web_designers=[]
    def __init__(self,Time_Of_Design,Name_customer,Cost_Of_Design,web_designers,**kwargs) -> None:
        self.Time_Of_Design=Time_Of_Design
        self.Name_customer=Name_customer
        self.Cost_Of_Design=Cost_Of_Design
        
        super().__init__(self,**kwargs)
        web_designers .append(self)
        
        
    def Income_web_designer(self):
         return self.Cost_Of_Design - self.Income
       
            
        
    
