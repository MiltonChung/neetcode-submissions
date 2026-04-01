class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROWS, COLS = len(matrix), len(matrix[0])
        numOfCells = ROWS * COLS
        currRow = 0
        currCol = 0
        layer = 0
        count = 0
        res = []

        while count < numOfCells:
            rightBoundary = COLS - layer
            bottomBoundary = ROWS - layer
            topBoundary = layer + 1
            leftBoundary = layer

            while currCol < rightBoundary and count < numOfCells:
                res.append(matrix[currRow][currCol])
                count += 1
                currCol += 1
            
            currCol -= 1
            currRow += 1

            while currRow < bottomBoundary and count < numOfCells:
                res.append(matrix[currRow][currCol])
                count += 1
                currRow += 1
            
            currRow -= 1
            currCol -= 1

            while currCol >= leftBoundary and count < numOfCells:
                res.append(matrix[currRow][currCol])
                count += 1
                currCol -= 1
            
            currCol += 1
            currRow -= 1

            while currRow >= topBoundary and count < numOfCells:
                res.append(matrix[currRow][currCol])
                count += 1
                currRow -= 1
            
            currRow += 1
            currCol += 1
            layer += 1
        
        return res