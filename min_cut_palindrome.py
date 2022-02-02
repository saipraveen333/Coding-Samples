def min_cut_palin(pal):
    l=[[0 for j in range(len(pal))]for i in range(len(pal))]
    r = []
    for j in range(1,len(pal)+1):
        i=0
        while j != len(pal):
            if not ispalindrome(pal[i:j + 1]):
                for k in range(i,j):
                    r.append(l[i][k]+l[k+1][j])
                l[i][j] =1+min(r)
            i+=1
            j+=1
            r.clear()
    return l[0][len(pal)-1]
def ispalindrome(i):
    return i[:]==i[::-1]
print(min_cut_palin('submadamsjhf'))

