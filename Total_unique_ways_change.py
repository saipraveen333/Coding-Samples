def total_unique_ways(n,arr):
    r=[0 for i in range(n+1)]
    r[0]=1
    for j in arr:
        for i in range(n + 1):
            if i >= j:
                r[i] = r[i] + r[i - j]
    return str(r[-1])+' ways'
print(total_unique_ways(5,[1,2,5]))