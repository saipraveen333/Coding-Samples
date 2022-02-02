def superior_element(a,l):
    for i in range(a+1,len(l)):
        if l[a]<=l[i]:
            return 'false'
    return 'true'
n=int(input())
l=list(map(int,input().split()))
count=0
for i in range(len(l)-1):
    if superior_element(i,l)=='true':
        count+=1
print(count+1)

