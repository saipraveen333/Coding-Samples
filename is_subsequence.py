def is_sub(arr,subs):
    d2 = [[False for j in range(len(arr))] for i in range(len(subs))]
    for i in range(len(subs)):
        for j in range(len(arr)):
            if i==0:
                if subs[i] == arr[j]:
                    d2[i][j] = True
                else:
                    d2[i][j]=d2[i][j-1]
            elif subs[i]==arr[j]:
                if d2[i-1][j]==True:
                    d2[i][j]=True
                else:
                    return False
            else:
                d2[i][j]=d2[i][j-1]
    return d2[-1][-1]
print(is_sub(['a','b','c','d','e','f','g'],['a','b','d']))