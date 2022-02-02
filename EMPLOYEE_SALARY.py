class employee:
    def __init__(self,empid,empname,emprole,empsalary):
        self.empid=empid
        self.empname=empname
        self.emprole=emprole
        self.empsalary=empsalary
    def increment_salary(self,number):
        increased_salary=self.empsalary*number//100
        return increased_salary

class organization:
    def __init__(self, orgname, employee_list):
        self.orgname = orgname
        self.employee_list = employee_list
    def calculate_salary(self,emprole,number):
        for i in self.employee_list:
            if i.emprole==emprole:
                obj1=employee(i.empid,i.empname,i.emprole,i.empsalary)
                print(i.empname)
                print(i.empsalary+obj1.increment_salary(number))
employee_list=[]
for i in range(int(input())):
    empid=int(input())
    empname=input()
    emprole=input()
    empsalary=int(input())
    employee_list.append(employee(empid,empname,emprole,empsalary))
emprole=input()
number=int(input())
obj2=organization('TATA',employee_list)
obj2.calculate_salary(emprole,number)


























