inp='(()())()())'
def rem_par(inp):
    count = 0
    l=[]
    def is_valid(set, count=0):
        for i in set:
            if i == '(':
                count += 1
            if i == ')':
                count += -1
            if count < 0:
                return False
        return count == 0
    def rem_par1(inp):
        for i in range(len(inp)):
            if is_valid(inp[:i] + inp[i + 1:]):
                if inp[:i] + inp[i + 1:] not in l:
                     print(inp[:i] + inp[i + 1:])
                     l.append(inp[:i] + inp[i + 1:])
    rem_par1(inp)
    return ''
print(rem_par(inp))
