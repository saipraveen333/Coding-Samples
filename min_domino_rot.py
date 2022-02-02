def min_dom_rot(arr):
    x=arr[0]
    y=arr[1]
    count1=1
    count2=1
    l=[]
    def minima1(x,y,a1,a2):
        for i in x:
            if i != x[0]:
                a1 += 1
        l.append(a1)
        for i in y:
            if i != x[0]:
                a2 += 1
        l.append(a2)
    def minima2(x,y,a1,a2):
        for i in x:
            if i != y[0]:
                a1 += 1
        l.append(a1)
        for i in y:
            if i != y[0]:
                a2 += 1
        l.append(a2)
    for i in range(len(x) - 1):
        if x[i + 1]==x[0] or y[i + 1]==x[0]:
            count1 += 1
    for i in range(len(y) - 1):
        if x[i + 1]==y[0] or y[i + 1]==y[0]:
            count2 += 1
        else:
            break
    if count1 != len(x) and count2 != len(x):
        return -1
    else:
        if count1==len(x):
            minima1(x,y,0,0)
        if count2 == len(y):
            minima2(x,y,0,0)
    return min(l)
arr=[[2,3,3,2,3],[3,5,3,3,4]]
print(min_dom_rot(arr))


