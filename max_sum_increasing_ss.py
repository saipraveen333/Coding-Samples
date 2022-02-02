def max_sum_inc_ss(arr):
    l=[]
    for i in arr:
        l.append(i)
    for i in range(1,len(arr)):
        for j in range(i):
            if arr[j]<=arr[i]:
                l[i]=max(l[i],arr[i]+l[j])

    return max(l) ,l
print(max_sum_inc_ss([5,10,67,30,40,60,4,70,6]))

