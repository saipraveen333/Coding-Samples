ans=[]
def NQueens(n,i,ans):
    if i==n:
        return True
    for j in range(n):
        if is_safe((i,j),ans):
            arr[i][j]=1
            ans.append((i,j))
            if NQueens(n,i+1,ans)==True:
                return True
            arr[i][j] = 0
    ans.pop()
    return False
def is_safe(pos,ans):
    for i,j in ans:
        if i==pos[0] or j==pos[1]:
            return False
        elif i-j==pos[0]-pos[1] or i+j==pos[0]+pos[1]:
            return False
    return True

arr=[[0 for i in range(6)]for j in range(6)]
NQueens(6,0,ans)
print(arr)
