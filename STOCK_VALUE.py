class payslip:
    def __init__(self,b,h,i):
        self.stockname=b
        self.stocksector=h
        self.stockvalue=i
class classDemo:
    def __init__(self,stocklist):
        self.stocklist=stocklist
    def getstocklist(self):
        for i in self.stocklist:
            if i.stocksector==given_sector:
                if i.stockvalue>500:
                    print(i.stockname)
stocklist=[]
for i in range(int(input())):
    stockname=input()
    stocksector=input()
    stockvalue=int(input())
    stocklist.append(payslip(stockname,stocksector,stockvalue))
given_sector=input()
obj=classDemo(stocklist)
obj.getstocklist()























