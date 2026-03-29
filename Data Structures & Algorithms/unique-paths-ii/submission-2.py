class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        cache = [[-1] * COLS for _ in range(ROWS)]

        def dfs(r, c):
            if r == ROWS or c == COLS:
                return 0
            if obstacleGrid[r][c] == 1:
                return 0
            if r == ROWS - 1 and c == COLS -1:
                return 1
            if cache[r][c] != -1:
                return cache[r][c]
            
            cache[r][c] = dfs(r + 1, c) + dfs(r, c + 1)
            return cache[r][c]

        return dfs(0, 0)