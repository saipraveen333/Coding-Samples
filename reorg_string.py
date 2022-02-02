d={}
ns=''
l=[]
m=[]
k=[]
def reorg_str(string,ns,d):
    for i in string:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    def sum_dict(d):
        for i, j in d.items():
            l.append(j)
        s = sum(l)
        return s
    while sum_dict(d)!=0:
        l.clear()
        for i, j in d.items():
            if j != 0:
                ns += i
                d[i]-=1
    for i in range(len(ns)-1,0,-1):
        if ns[i]==ns[i-1]:
            m.append(ns[i])
        else:
            ns = ns[:i+1]
            break
    for i in ns:
       k.append(i)
    i=0
    cc=len(m)
    while cc!=0 and i<=len(ns):
        if k[i]!=ns[-1] and k[i+1]!=ns[-1]:
             k.insert(i+1,ns[-1])
             cc-=1
        i+=1
    if k[0]!=ns[-1]:
        k.insert(0,ns[-1])
        cc-=1
    if cc==0:
        s=''
        for i in k:
            s+=i
        return s
    else:
        return -1


    #return ns,m,k,i
print(reorg_str('caaaaaaarcvusuivaoisvnannnbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbsihdsbdttilage','',d))
