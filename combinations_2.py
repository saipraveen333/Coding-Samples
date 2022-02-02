def combs(k,n):
    l=[i for i in range(1,n+1)]
    r=[]
    def sol(l,li):
        if len(li)==k:
            r.append(li)
            return
        for i in range(len(l)):
            sol(l[i+1:],li+[l[i]])
    sol(l,[])
    return r
print(combs(2,3))


