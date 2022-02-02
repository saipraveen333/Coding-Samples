l=[]
def comb_sum(a,target,index,sub_str):
    if sum(sub_str)==8:
        l.append(sub_str.copy())
    if target<0:
        return
    for i in range(index,len(a)):
        sub_str.append(a[i])
        comb_sum(a, target-a[i], i, sub_str)
        sub_str.remove(a[i])
print(comb_sum([2,3,5],8,0,[]))
print(l)