l = [int(i) for i in input().split()]
W = l[0]
H = l[1]
N = l[2]
M = l[3]
Nlist = [int(i) for i in input().split()]
Mlist = [int(i) for i in input().split()]
k=0
luck=False
greatest_number=-1
Mdist = ()
for i in range(M-1):
    for j in range(M-1, i, -1):
        Mdist += (abs(Mlist[j] - Mlist[i]),)
temp=Mdist
Ndist = ()
for i in range(N - 1):
    for j in range(N - 1, i, -1):
        Ndist += (abs(Nlist[j] - Nlist[i]),)
for i in range(H+1):
    if i==Mlist[k]:
        continue
    else:
        for j in range(M):
            Mdist += (abs(i - Mlist[j]),)
    print(Mdist)
    Mdist = set(Mdist)
    Ndist = set(Ndist)
    total_squares = Mdist&Ndist
    if len(total_squares)==N:
        luck=True
        print(len(total_squares))
        break
    else:
        current_number=len(total_squares)
        if current_number>greatest_number:
            greatest_number=current_number
    Mdist=temp
if luck==False:
    print(greatest_number)




