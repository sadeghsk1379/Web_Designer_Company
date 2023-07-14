from person import Person
from department_employees import Department_Employees
class sale(Person,Department_Employees):
    Sales_Employees=[]
    def __init__(self,Sales_Number,Sales_Profit,Date_Sale,Buyer,Job,sales_Employees, **kwargs) -> None:
        self.Sales_Number=Sales_Number
        self.Sales_Profit=Sales_Profit
        self.Date_Sale=Date_Sale
        self.Buyer=Buyer
        self.Job=Job
        
        super().__init__(self,**kwargs)
        sales_Employees.append(self)
        
        
    
        
    
    pass
