l=[]
arr=[5,2,[7,-1],3,[6,[-13,8,4,-4],4]]
def product_sum(arr,mul=1):
    sum=0
    for i in arr:
        if type(i) is list:
            sum+=product_sum(i,mul+1)
        else:
            sum+=i
    return sum*mul

print(product_sum(arr))
r='123'
def permutations(r):
    if len(r)==1:
        return r
    first = r[0]
    list=[]
    perms = permutations(r[1:])

    for per in perms:
        for i in range(len(per) +1):
            perm = per[:i] + first + per[i:]
            list.append(perm)

    return list
print(permutations(r))



