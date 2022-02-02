from collections import deque
class stack:
    def __init__(self):
        self.c=deque()
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
def reverse_string(str):
    s = stack()

    for ch in str:
        s.push(ch)

    rstr = ''
    while s.size()!=0:
        rstr += s.pop()

    return rstr



print(reverse_string("We will conquer COVID-19"))




