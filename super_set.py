arr=[1,2,3,4]
l=[[]]
for i in arr:
    for j in range(len(l)):
        l.append(l[j]+[i])
print(l)
arr=['a','b','c','d']
def super_set(arr):
    l = [[]]
    for i in arr:
        for j in l:
            if len(j) == 0:l.append([i])
            elif (j[-1]) < i: l.append(j + [i])
    return l
print(super_set(arr))
def power_set(arr,index=None):
    if index is None:
        index=len(arr)-1
    if index <0:
        return  [[]]
    l=power_set(arr,index-1)
    for i in range(len(l)):
        l.append(l[i]+[arr[index]])
    return l
print(power_set([1,2,3]))
















