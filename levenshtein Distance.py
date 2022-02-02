def lav_dist(s1,s2):
    l=[[0 for i in range(len(s2))]for i in range(len(s1))]
    for i in range(len(s2)):
        if s1[0]!=s2[i]:
           l[0][i]=l[0][i-1]+1
        else:
            l[0][i]=l[0][i-1]
    for i in range(len(s1)):
        if s1[i]==s2[0]:
            l[i][0]=l[i-1][0]
        else:
            l[i][0]=l[i-1][0]+1
    for i in range(1,len(s1)):
        for j in range(1,len(s2)):
            if s1[i] == s2[j]:
                l[i][j]=l[i-1][j-1]
            else:
                l[i][j] = 1+min(l[i - 1][j - 1],l[i - 1][j],l[i][j - 1])
    return l[-1][-1]
print(lav_dist('svsjh','yabdujkshu'))