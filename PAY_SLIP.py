class payslip:
    def __init__(self,b,h,i):
        self.basicSalary=b
        self.hra=h
        self.ita=i
class PaySlipDemo:
    def __init__(self,payslip_list):
        self.payslip_list=payslip_list
    def getHighestPF(self):
        import math
        highest_salary=-math.inf
        for i in self.payslip_list:
            if i.basicSalary>highest_salary:
                highest_salary=i.basicSalary
        print(int(highest_salary*12/100))
payslip_list=[]
for i in range(int(input())):
    basicSalary=int(input())
    hra=int(input())
    ira=int(input())
    payslip_list.append(payslip(basicSalary,hra,ira))
obj=PaySlipDemo(payslip_list)
obj.getHighestPF()























