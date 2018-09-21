### Hieu Trinh
### ICP 4 - Task 1
### 09/14/18

#Employee - keep track of employees
class Employee:
    employeeNum = 0
    totalSalary = 0.0
    
    #Initial
    def __init__(self,n,f,s,d):
        Employee.employeeNum += 1
        Employee.totalSalary += s
        self.name = n
        self.family = f
        self.salary = s
        self.department = d
        
    def returnSalary(self):
        return str(self.salary)
    
    def returnEmployeeNum(self):
        return str(self.__class__.employeeNum)
    
    #Return average salary of all employees
    def averageSalary(self):
        if self.__class__.employeeNum == 0:
            print ("There are no employees.")
            return 0
        else:
            return self.totalSalary/self.employeeNum
            
class FullTimeEmployee (Employee):
    def __init__(self,s):
        Employee.employeeNum += 1
        Employee.totalSalary += s
        self.name = "John Smith"
        self.ID = "23"
    
    def returnInfo(self):
        return self.name + " - " + self.ID
        
        
emp1 = Employee("Elisa","Levi",300,"Mathematics")
print("Hello, I am " + emp1.name + " " + emp1.family + ". I am in " + emp1.department + " Department, and my salary is $" + emp1.returnSalary() + ".")
print("There is currently " + emp1.returnEmployeeNum() + " employees in my company, and the average salary is $" + str(emp1.averageSalary()) + ".\n")

emp2 = Employee("Bob","Erin",425,"Computer Science")
print("There are currently " + emp2.returnEmployeeNum() + " employees in my company, and the average salary is $" + str(emp2.averageSalary()) + ".\n")

emp3 = FullTimeEmployee(575)
print("I am a new full-time employee. My name is " + emp3.returnInfo() + ". There are currently " + emp3.returnEmployeeNum() + " employees in my company, and the average salary is $" + str(emp3.averageSalary()) + ".\n")

emp4 = FullTimeEmployee(300)
print("There are currently " + emp4.returnEmployeeNum() + " employees in my company, and the average salary is $" + str(emp4.averageSalary()) + ".")

### END ###