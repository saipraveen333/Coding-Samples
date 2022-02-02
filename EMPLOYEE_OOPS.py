class Employee:
    def __init__(self,n,d,s,lb):
        self.name=n
        self.designation=d
        self.salary=s
        self.leaveBalance=lb
class Organization:
    def __init__(self,elist):
        self.employee_list=elist
    def checkLeaveEligibility(self,empname,tl,nol):
        for i in self.employee_list:

            if i.name==empname:
                for a,b in i.leaveBalance.items():
                    if a==tl:
                        if b>=nol:
                            i.leaveBalance[a]=b-nol

                            return 'True'
                        else:
                            return 'False'
        return 'not_found'
    def display_details(self,name):
        for i in self.employee_list:
            if i.name==name:
                for a,b in i.leaveBalance.items():
                     print(a+':'+str(b))
elist=[]
num=int(input())
for i in range(num):
    leaves={}
    name=str(input())
    designation=str(input())
    salary=int(input())
    for j in range(int(input())):
        tl=str(input())
        nol=int(input())
        leaves[tl]=nol
    elist.append(Employee(name,designation,salary,leaves))


obj=Organization(elist)
empname=str(input())

tl=str(input())
nol=int(input())
if (obj.checkLeaveEligibility(empname,tl,nol)=='True'):
    print('Leave Granted')
    obj.display_details(empname)
elif obj.checkLeaveEligibility(empname, tl, nol) == 'False':
    print('Leave Not Granted')
    obj.display_details(empname)
elif obj.checkLeaveEligibility(empname, tl, nol) == 'not_found':
    print('Leave Not Granted')
    print('No Employee Found')






















