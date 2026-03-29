class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        box = defaultdict(set)
        ROWS, COLS = len(board), len(board[0])

        for r in range(ROWS):
            for c in range(COLS):
                value = board[r][c]
                if value == '.':
                    continue
                if (value in rows[r] or
                    value in cols[c] or
                    value in box[(r // 3, c // 3)]):
                    return False
                
                rows[r].add(value)
                cols[c].add(value)
                box[(r // 3, c // 3)].add(value)
        
        return True