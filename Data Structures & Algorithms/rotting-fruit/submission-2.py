class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        res = 0
        
        for r in range(len(grid)):
          for c in range(len(grid[r])):
            if grid[r][c] == 2:
              queue.append((r, c, 0))
              
        while queue:
          r, c, time = queue.popleft()
          for dr, dc in directions:
            newR = r + dr
            newC = c + dc

            if (min(newR, newC) < 0 or
                newR == ROWS or newC == COLS or
                grid[newR][newC] != 1):
                if time > res:
                  res = time
                continue
            queue.append((newR, newC, time + 1))
            grid[newR][newC] = 2

        for r in range(len(grid)):
          for c in range(len(grid[r])):
            if grid[r][c] == 1:
              return -1
        
        return res