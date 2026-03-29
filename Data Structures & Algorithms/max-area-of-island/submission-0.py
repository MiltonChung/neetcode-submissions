class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0

        for r, _ in enumerate(grid):
            for c, _ in enumerate(grid[r]):
                if grid[r][c] == 1:
                    area = self.dfs(grid, r, c)
                    if area > maxArea:
                        maxArea = area
        return maxArea

    def dfs(self, grid: List[List[int]], r: int, c: int) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        if min(r, c) < 0 or r == ROWS or c == COLS or grid[r][c] == 0:
            return 0

        grid[r][c] = 0
        area = 0
        area += self.dfs(grid, r + 1, c)
        area += self.dfs(grid, r - 1, c)
        area += self.dfs(grid, r, c + 1)
        area += self.dfs(grid, r, c - 1)

        return area + 1
