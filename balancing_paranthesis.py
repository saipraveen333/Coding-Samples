from collections import deque
class stack:
    def __init__(self):
        self.c=deque()
    def count(self,val,str):
        count=0
        for i in str:
            if i==val:
                count+=1
        return count
    
    def append(self,val):
        self.c.append(val)
    def pop(self):
        return self.c.pop()
    def peek(self):
        return self.c[-1]
    def push(self,val):
        self.c.append(val)
    def size(self):
        return len(self.c)

s=stack()
def is_balanced(str):
    s=stack()
    m={'(':')','[':']','{':'}'}
    for i in str:
        if i=='(' or i=='['or i=='{':
            s.push(i)
        if i==')' or i==']' or i=='}':
            if s.size()==0:
                return False
            if i!=m[s.pop()]:
                return False
    return s.size()==0

print(is_balanced('(()){}sddfh'))



