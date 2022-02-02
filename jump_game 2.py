def min_jump(arr):
    l=[]
    def min_jump1(arr,ele,i,c):
        if i == len(arr)-1:
            l.append(c)
            return
        if i > len(arr)-1:
            return
        for k in range(ele,0,-1):
            min_jump1(arr,arr[k],i+k,c+1)
    min_jump1(arr,arr[0],0,0)
    return min(l)
arr=[1,2,1,1,4]
print(min_jump(arr))