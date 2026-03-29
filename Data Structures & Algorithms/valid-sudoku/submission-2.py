class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hashset = set()
        ROWS, COLS = len(board), len(board[0])

        # Check rows
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == '.':
                    continue
                if board[r][c] in hashset:
                    return False
                hashset.add(board[r][c])
            hashset.clear()

        # Check columns
        for c in range(COLS):
            for r in range(ROWS):
                if board[r][c] == '.':
                    continue
                if board[r][c] in hashset:
                    return False
                hashset.add(board[r][c])
            hashset.clear()

        def checkSubboxes(startR, startC):
            for r in range(startR, startR + 3):
                for c in range(startC, startC + 3):
                    if board[r][c] == '.':
                        continue
                    if board[r][c] in hashset:
                        return False
                    hashset.add(board[r][c])
            hashset.clear()
            return True

        for r in range(0, ROWS, 3):
            for c in range(0, COLS, 3):
                if not checkSubboxes(r, c):
                    return False

        return True
