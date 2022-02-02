class HashTable:
    def __init__(self):
        self.max=100
        self.arr=[None for i in range(self.max)]
    def get_hash(self,key):
        h=0
        for i in key:
            h+=ord(i)
        return h%100
    def add(self,key,val):
        h=self.get_hash(key)
        self.arr[h]=val
    def get(self,key):
        h = self.get_hash(key)
        return self.arr[h]
    def _del_(self,key):
        h = self.get_hash(key)
        self.arr[h]=None
    def print(self):
        hh=''
        for i in self.arr:
            if i!=None:
               hh+=str(i)+','
        hh=hh[:-1]
        print(hh)



ht=HashTable()
ht.add('A',1)
ht.add('b',2)
ht.add('c',3)
ht.print()
