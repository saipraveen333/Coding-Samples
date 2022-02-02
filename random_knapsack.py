l=[]
Xlist=[10, 30, 27,32]
Alist=[2,7, 25, 3, 17, 8]
sums=[]
indices=[]
def comb_sum(a,target,index,sub_str,indices):
    if sum(sub_str) in Xlist:
        if sum(sub_str) not in sums:
            l.append(indices.copy())
            sums.append(sum(sub_str))
        return
    if target<0:
        return
    for i in range(index,len(a)):
        sub_str.append(a[i])
        indices.append(i+len(Alist)-len(a))
        comb_sum(a[1:], target-a[i], i, sub_str,indices)
        sub_str.remove(a[i])
        indices.pop()
comb_sum(Alist,max(Xlist),0,[],indices)
#print(l)
#print(indices)
'''
6
2 7 25 3 17 8
3
10 30 27
'''
Y=0
Ylist=[]
for i in l:
    for j in range(len(i)):
        Y+=2**(i[j]-1)
    Ylist.append(Y)
    Y=0
for i in Ylist:
    print(int(i%2**60),int((i//2**60)%2**60),int((i//2**120)%2**60),int((i//2**180)%2**60))

