#insertion sort
r=[5,3,8,9,10,2,3,7,8,2,5]
for i in range(1,len(r)):
    for j in range(i):
        if r[i]<r[j]:
            r.insert(j,r[i])
            r.pop(i+1)
#print(r)

#selection sort
r=[5,3,8,9,10,2,3,7,8,2,5]
s=[]
for i in range(len(r)):
    k=i
    for j in range(i+1,len(r)):
        if r[k]>r[j]:
            k=j
    r[k],r[i]=r[i],r[k]
print(r)
#bubble sort
for i in range(len(r)-1):
    for j in range(i+1,len(r)):



