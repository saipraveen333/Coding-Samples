import math
def min_no_of_coins(n,arr):
    l=[math.inf for i in range(n+1)]
    l[0]=0
    for i in arr:
        for j in range(n+1):
            if j>=i:
                l[j]=min(l[j],l[j-i]+1)
    return l[-1]
print(min_no_of_coins(1,[1,2,5]))