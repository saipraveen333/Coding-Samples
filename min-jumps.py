def min_jumps(arr):
    m=[]
    l=[0 for i in range(len(arr))]
    #print(l)
    for i in range(1,len(arr)):
        for j in range(i):
            if arr[j]>=i-j:
                m.append(l[j])
        l[i]=min(m)+1
        m.clear()
    for i in range(1,len(arr)):
        if l[i]!=l[i-1]:
            m.append(arr[i])
    return l[-1],m+[arr[-1]]
print(min_jumps([3,4,2,1,2,3,7,1,1,1,3,4,6,2]))