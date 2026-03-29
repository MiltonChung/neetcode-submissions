class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(board) < 1 or len(word) < 1:
            return False

        ROW, COL = len(board), len(board[0])
        visited = set()

        def dfs(i, j, c):
            if c == len(word):
                return True
            if i == ROW or i < 0 or j == COL or j < 0:
                return False
            if board[i][j] != word[c]:
                return False
            if (i, j) in visited:
                return False
            
            visited.add((i, j))
            
            res = (dfs(i - 1, j, c + 1) or
                   dfs(i, j + 1, c + 1) or
                   dfs(i + 1, j, c + 1) or
                   dfs(i, j - 1, c + 1))
            
            visited.remove((i, j))
            return res

        for i in range(ROW):
            for j in range(COL):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True

        return False