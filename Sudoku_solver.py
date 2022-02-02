board = [
    [0,0,0,2,0,0,5,0,3],
    [0,0,5,0,8,0,0,6,0],
    [0,0,6,0,1,9,0,7,0],
    [2,0,1,0,0,0,0,0,0],
    [5,0,4,0,0,0,8,0,6],
    [0,0,0,0,0,0,3,0,2],
    [0,8,0,6,2,0,9,0,0],
    [0,5,0,0,3,0,7,0,0],
    [9,0,3,0,0,7,0,0,0]
]

def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if is_valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False
def out_board(board):
    for i in range(len(board)):
        if i%3==0 and i!=0:
            print('- - - - - - - - - - ')
        for j in range(len(board[0])):
            if j%3==0 and j!=0:
                print('|',end='')
            if j==8:
                print(board[i][j])
            else:
                print(str(board[i][j])+' ',end='')
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]==0:
                return (i,j)
    return None
def is_valid(board,num,pos):
    #box
    for i in range(len(board[0])):
            if num==board[pos[0]][i] and i!=pos[0]:
                return False
    #column
    for i in range(len(board)):
            if num==board[pos[1]][i] and i!=pos[1]:
                return False
    #box
    a=pos[0]//3
    b=pos[1]//3
    for i in range(a*3,a*3+3):
        for j in range(b*3,b*3+3):
            if num==board[i][j] and (i,j)!=pos:
                return False
    return True



#print(out_board(board))
solve(board)
out_board(board)
