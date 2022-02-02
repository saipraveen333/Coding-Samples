def max_ss_sum(arr):
    l=[]
    m=[]
    ans=[]
    r=[-1 for i in range(len(arr))]
    for i in arr:
        l.append(i)
    for i in range(2,len(arr)):
        for j in range(i-1):
            if arr[i]+l[j]>l[i]:
                l[i]=arr[i]+l[j]
                r[i]=j
    q = l.index(max(l))
    while (q != -1):
        m.append(q)
        q = r[q]
    for i in m:
        ans.append(arr[i])
    return str(max(l))+str(tuple(ans[::-1]))
print(max_ss_sum([2,3,7,8,10]))