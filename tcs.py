class Food:
    def __init__(self,name,proteins,fat,carbohydrates,energy,status):
        self.name=name
        self.proteins = proteins
        self.fat = fat
        self.carbohydrates= carbohydrates
        self.energy = energy
        self.status = status
class Nutrition:
    def __init__(self,energydict,foodlist):
        self.energydict=energydict
        self.foodlist=foodlist
    def setEnergy(self,foodlist):
        print('Energy of Food:')
        for i in foodlist:
            i.energy=i.proteins+i.fat+i.carbohydrates
            for j in self.energydict:
                if energydict[j][0]<=i.energy and energydict[j][1]>=i.energy:
                    #print(i.energy)
                    rand=j
                    print(i.name , '-' , i.energy , '-' , rand)
    def getEnergyRichFood(self,status):
        l=[]
        for i in self.foodlist:
            if i.energy<=status:
                l.append(i)
        if len(l)==0:
            return None
        else:
            print('Food within given criteria:')
            for i in l:
                print(i.name,':',i.energy)
foodlist=[]
for i in range(int(input())):
    name=input()
    proteins=float(input())
    fat =float(input())
    carbohydrates=float(input())
    foodlist.append(Food(name, proteins, fat, carbohydrates, proteins + fat + carbohydrates, 0))
energydict={}
for i in range(int(input())):
    a=input()
    b1=int(input())
    b2=int(input())
    if b1>b2:
            b1,b2=b2,b1
    tp=[]
    tp.append(b1)
    tp.append(b2)
    tp=tuple(tp)
    energydict[a]=tp
status=int(input())

nut=Nutrition(energydict,foodlist)
nut.setEnergy(foodlist)
nut.getEnergyRichFood(status)
if nut.getEnergyRichFood(status)==None:
    print('No food found')



















