def disk_stack(arr):
    r=[-1 for i in range(len(arr))]
    arr=sorted(arr,reverse=True)
    l=[]
    m=[]
    ans=[]
    for i in arr:
        l.append(i[-1])
    for i in range(1,len(arr)):
        for j in range(i):
            if arr[j][0]>arr[i][0] and arr[j][1]>arr[i][1] and arr[j][2]>arr[i][2]:
                l[i]=max(l[i],arr[i][-1]+l[j])
                r[i]=j
    q=l.index(max(l))
    while(q!=-1):
        m.append(q)
        q=r[q]
    for i in m:
        ans.append(arr[i])
    return ans
print(disk_stack([[5,3,10],[2,1,2],[1,0,1],[3,2,3],[2,2,8],[2,3,4],[1,3,1],[4,4,5],[10,10,1]]))


