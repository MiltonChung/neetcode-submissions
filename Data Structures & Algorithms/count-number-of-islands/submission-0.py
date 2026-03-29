class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        for r,_ in enumerate(grid):
            for c,_ in enumerate(grid[r]):
                if grid[r][c] == '1':
                    self.dfs(grid, r, c)
                    count += 1

        return count

    def dfs(self, grid: List[List[str]], r: int, c: int) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        if (min(r, c) < 0 or
            r == ROWS or c == COLS or
            grid[r][c] == '0'):
            return
        if grid[r][c] == '1':
            grid[r][c] = '0'

        self.dfs(grid, r + 1, c)
        self.dfs(grid, r - 1, c)
        self.dfs(grid, r, c + 1)
        self.dfs(grid, r, c - 1)
        return
