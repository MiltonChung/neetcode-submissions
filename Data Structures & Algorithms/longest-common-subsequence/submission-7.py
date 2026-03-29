class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        ROWS, COLS = len(text1), len(text2)
        text1Arr, text2Arr = list(text1), list(text2)
        grid = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        for i in range(ROWS - 1, -1, -1):
            for j in range(COLS - 1, -1, -1):
                if text1Arr[i] == text2Arr[j]:
                    # print(i, j, grid, COLS - 1)
                    # if j == COLS - 1 or i == ROWS - 1:
                    #     grid[i][j] += 1
                    # else:
                    grid[i][j] = grid[i+1][j+1] + 1
                else:
                    # right = grid[i][j+1] if j != COLS - 1 else 0
                    # bottom = grid[i+1][j] if i != ROWS - 1 else 0
                    right = grid[i][j+1] 
                    bottom = grid[i+1][j]

                    grid[i][j] = max(right, bottom)
        
        return grid[0][0]