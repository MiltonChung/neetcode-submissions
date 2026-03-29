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

        def checkSubboxes(startR, endR, startC, endC):
            for r in range(startR, endR + 1):
                for c in range(startC, endC + 1):
                    if board[r][c] == '.':
                        continue
                    if board[r][c] in hashset:
                        return False
                    hashset.add(board[r][c])
            hashset.clear()
            return True

        if not checkSubboxes(0, 2, 0, 2): return False
        if not checkSubboxes(0, 2, 3, 5): return False
        if not checkSubboxes(0, 2, 6, 8): return False
        if not checkSubboxes(3, 5, 0, 2): return False
        if not checkSubboxes(3, 5, 3, 5): return False
        if not checkSubboxes(3, 5, 6, 8): return False
        if not checkSubboxes(6, 8, 0, 2): return False
        if not checkSubboxes(6, 8, 3, 5): return False
        if not checkSubboxes(6, 8, 6, 8): return False

        return True