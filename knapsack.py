def knap_sack(n,arr):
    l=[[0 for i in range(n+1)]for j in range(len(arr))]
    v=[i[0] for i in arr]
    w=[i[1] for i in arr]
    for i in range(len(arr)):
        for j in range(n+1):
            if j>=w[i]:
                l[i][j]=max(l[i-1][j],v[i]+l[i-1][j-w[i]])
            else:
                l[i][j]=l[i-1][j]
    Theweights=weights(w,arr,l,v,n)
    return l,Theweights
def weights(w,arr,l,v,n):
    wr=[]
    i=len(arr)-1
    j=n
    while(l[i][j]!=0):
        while l[i][j]==l[i-1][j]:
            i=i-1
        wr.append(w[i])
        j = j -w[i]
        i=i-1
    return wr




print(knap_sack(10,[[1,2],[4,3],[5,6],[6,7]]))