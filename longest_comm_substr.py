def long_comm_substr(s1,s2):
    l=[[0 for i in range(len(s1)+1)]for j in range(len(s2)+1)]
    for i in range(1,len(s2)+1):
        for j in range(1,len(s1)+1):
            if s1[j-1]==s2[i-1]:
                l[i][j]=l[i-1][j-1]+1
            else:
                l[i][j]=max(l[i-1][j],l[i][j-1])
    for i in l:
        print(i)
    #return l
print(long_comm_substr('xkykzpw','zxvvyzw'))