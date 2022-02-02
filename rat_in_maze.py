maze=[[1,0,0,0],
      [1,1,0,1],
      [0,1,0,0],
      [1,1,1,1]]
def rat_in_maze(maze):
    i=0
    j=0
    def rat_in_maze1(i,j,maze):
        if i == len(maze)-1 and j == len(maze)-1:
            return
        if maze[i][j+1]==1 and j+1<=len(maze[0])-1:
            print(i,j+1)
            rat_in_maze1(i, j+1, maze)
        elif maze[i+1][j]==1 and i+1<=len(maze)-1:
            print(i+1,j)
            rat_in_maze1(i+1, j, maze)
    rat_in_maze1(i, j, maze)
    return ''
print(rat_in_maze(maze))