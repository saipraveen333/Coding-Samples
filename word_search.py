board=[['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]
word='ABF'
def exist(board, word):
        m = len(board)
        if m == 0:
            return False
        n = len(board[0])

        def dfs(i, j, word):
            if not word:
                return True
            if not (0 <= i < m and 0 <= j < n):
                return False
            if word[0] != board[i][j]:
                return False
            tmp = board[i][j]
            board[i][j] = '#'
            res = dfs(i - 1, j, word[1:]) or dfs(i + 1, j, word[1:]) or \
                dfs(i, j - 1, word[1:]) or dfs(i, j + 1, word[1:])
            board[i][j] = tmp

            return res

        for i in range(m):
            for j in range(n):
                if dfs(i, j, word):
                    return True

        return False
print(exist(board, word))