class HashTable:
    def __init__(self):
        self.max=10
        self.arr=[[] for i in range(self.max)]
    def get_hash(self,key):
        h=0
        for i in key:
            h+=ord(i)
        return h%10
    def add(self,key,value):
        h=self.get_hash(key)
        q=False
        for i,j in enumerate(self.arr[h]):
                if j[0]==key:
                    print(i,j)
                    self.arr[h][i]=(key,value)
                    q=True
                    break
        if not q:
            self.arr[h].append([key,value])
    def print(self):
        hh=''
        for i in self.arr:
            if i!=[]:
               hh+=str(i)+','
        hh=hh[:-1]
        print(hh)
ht=HashTable()
ht.add('a',1)
ht.add('march 6',2)
ht.add('march 17',6)
ht.add('march 6',6)
ht.print()