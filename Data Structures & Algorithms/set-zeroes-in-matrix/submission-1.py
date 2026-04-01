class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])

        # Mark all original 0s
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[r][c] = None

        # update to 0 for all directions
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == None:
                    top = 0
                    right = COLS - 1
                    bottom = ROWS - 1
                    left = 0

                    matrix[r][c] = 0

                    # top
                    for i in range(r, top - 1, -1):
                        if matrix[i][c] is not None:
                            matrix[i][c] = 0 
                    
                    # right
                    for i in range(c, right + 1):
                        if matrix[r][i] is not None:
                            matrix[r][i] = 0

                    # bottom
                    for i in range(r, bottom + 1):
                        if matrix[i][c] is not None:
                            matrix[i][c] = 0
                    
                    # left
                    for i in range(c, left - 1, -1):
                        if matrix[r][i] is not None:
                            matrix[r][i] = 0
