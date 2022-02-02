maze=[[1 ,1 ,1, 1, 1,1, 1, 1,  1 , 1 ],
[1 , 0 , 1 , 1 , 1,  1 , 1 , 1,  1 , 1 ],
[1 , 1 , 1 , 0 , 1  ,1  ,1 , 1,  1 , 1 ],
[1  ,1 , 1 , 1 , 0 , 1 , 1 , 1 , 1 , 1 ],
[1 , 1 , 1 , 1 , 1 , 1  ,1  ,1  ,1  ,1 ],
[1  ,1 , 1 , 1 , 1,  0 , 1 , 1  ,1 , 1 ],
[1 , 0 , 1 , 1 , 1 , 1 , 1 , 1 , 0 , 1 ],
[1 , 1 ,1,  1 , 1 , 1  ,1  ,1  ,1  ,1 ],
[1  ,1  ,1  ,1  ,1  ,1  ,1,  1,  1 , 1 ],
[0  ,1  ,1 ,1  ,1  ,0  ,1 , 1 , 1 , 1 ],
[1 , 1,  1 , 1,  1 , 1 , 1 , 1 , 1 , 1 ],
[1  ,1  ,1  ,0,  1,  1 , 1  ,1  ,1  ,1 ]]
def min_safe_route1(maze):
    l=[]
    def min_safe_route(i,j,count):
        if j == len(maze[0])-1:
            l.append(count)
            print(count)
            count-=1
            return count
        temp=maze[i][j]
        maze[i][j]=0
        if j + 1 <= len(maze[0]) - 1 and maze[i][j+1]==1:
            count+=1
            min_safe_route(i, j + 1,count)
        if i + 1 <= len(maze) - 1 and maze[i+1][j]==1:
            count += 1
            min_safe_route(i + 1, j,count)
        if i - 1 >= 0 and maze[i-1][j]==1:
            count += 1
            min_safe_route(i - 1, j,count)
        if j - 1 >= 0 and maze[i][j-1]==1:
            count += 1
            min_safe_route(i, j - 1,count)
        maze[i][j]=temp
    for i in range(len(maze)):
        min_safe_route(i,0,1)
    return 'the smallest is'+' '+str(min(l))

print(min_safe_route1(maze))

