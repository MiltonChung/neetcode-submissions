class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        prevRow = [0] * COLS
        
        for r in range(ROWS - 1, -1, -1):
            curRow = [0] * COLS
            lastCol = 0
            for c in range(COLS - 1, -1, -1):
                if obstacleGrid[r][c] == 1:
                    curRow[c] = 0
                    lastCol = 0
                    continue
                
                if r == ROWS - 1 and c == COLS - 1:
                    curRow[c] = 1
                else:
                    curRow[c] = lastCol + prevRow[c]
                
                lastCol = curRow[c]
            prevRow = curRow
        
        return prevRow[0]