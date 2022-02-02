def permutations(list):
    if len(list)==1:
        return list
    l = []
    perms=permutations(list[1:])
    first=list[0]
    for perm in perms:
        for i in range(len(perm)+1):
            l.append(perm[:i]+first+perm[i:])
    return l

list='1234'

print(permutations(list))