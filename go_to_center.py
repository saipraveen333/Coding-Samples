maze=[[ 3, 5, 4, 4, 7, 3, 4, 6, 3 ],
[ 6, 7, 5, 6, 6, 2, 6, 6, 2 ],
[ 3, 3, 4, 3, 2, 5, 4, 7, 2 ],
[ 6, 5, 5, 1, 2, 3, 6, 5, 6 ],
[ 3, 3, 4, 3, 0, 1, 4, 3, 4 ],
[ 3, 5, 4, 3, 2, 2, 3, 3, 5 ],
[ 3, 5, 4, 3, 2, 6, 4, 4, 3 ],
[ 3, 5, 1, 3, 7, 5, 3, 6, 4 ],
[ 6, 2, 4, 3, 4, 5, 4, 5, 1 ]]
def go_to_center(maze):
    i=0
    j=0
    s=''
    def go_to_center2(i,j,s):
        if i==len(maze)//2 and j==len(maze)//2:
            print(s[:-3])
            return
        if maze[i][j]==0:
            return
        m = maze[i][j]
        maze[i][j] = 0
        if j+m<=len(maze)-1:
            s+='('+str(i)+','+str(j+m)+')'+'-->'
            go_to_center2(i,j+m,s)
        if j-m>0:
            s+='('+str(i)+','+str(j-m)+')'+'-->'
            go_to_center2(i,j-m,s)
        if i-m>=0:
            s+='('+str(i-m)+','+str(j)+')'+'-->'
            go_to_center2(i-m,j,s)
        if i+m<=len(maze)-1 :
            s+='('+str(i+m)+','+str(j)+')'+'-->'
            go_to_center2(i+m,j,s)
        maze[i][j]=m
    go_to_center2(i,j,s)
    return s
print(go_to_center(maze))








