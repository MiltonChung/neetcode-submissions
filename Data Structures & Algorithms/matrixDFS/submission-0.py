class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        visited = set()
        return self.dfs(grid, 0, 0, visited)
    
    def dfs(self, grid: List[List[int]], r: int, c: int, visited) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        if (min(r, c) < 0 or r == ROWS or c == COLS or
            grid[r][c] == 1 or (r, c) in visited):
            return 0
        
        if r == ROWS - 1 and c == COLS - 1:
            return 1
        
        visited.add((r, c))

        count = 0
        count += self.dfs(grid, r + 1, c, visited)
        count += self.dfs(grid, r - 1, c, visited)
        count += self.dfs(grid, r, c + 1, visited)
        count += self.dfs(grid, r, c - 1, visited)

        visited.remove((r,c))
        return count