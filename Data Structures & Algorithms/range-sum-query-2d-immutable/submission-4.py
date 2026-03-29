class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # prefix matrix with padding top and left
        self.prefix = [[0] * (len(matrix[0])) for _ in range(len(matrix))]
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                rowAbove = self.prefix[row - 1][col] if row - 1 >= 0 else 0
                colBefore = self.prefix[row][col - 1] if col - 1 >= 0 else 0
                diagBefore = self.prefix[row - 1][col - 1] if col - 1 >= 0 and row - 1 >= 0 else 0
                self.prefix[row][col] = rowAbove + colBefore + matrix[row][col] - diagBefore
        print(self.prefix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        allSum = self.prefix[row2][col2]
        topRow = self.prefix[row1 - 1][col2] if row1 - 1 >= 0 else 0
        leftCol = self.prefix[row2][col1 - 1] if col1 - 1 >= 0 else 0
        topLeft = self.prefix[row1 - 1][col1 - 1] if col1 - 1 >= 0 and row1 - 1 >= 0 else 0

        return allSum - topRow - leftCol + topLeft
