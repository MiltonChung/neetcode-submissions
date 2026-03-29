class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        queue = deque()
        hasReachedEnd = False
        visit.add((0, 0))
        queue.append((0, 0))
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        if grid[0][0] == 1 or grid[ROWS-1][COLS-1] == 1:
            return -1

        length = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if grid[r][c] == 1:
                    return -1
                if r == ROWS - 1 and c == COLS - 1:
                    hasReachedEnd = True
                    return length
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (min(nr, nc) < 0 or
                        nr == ROWS or nc == COLS or
                        grid[nr][nc] == 1 or
                        (nr, nc) in visit):
                        continue
                    queue.append((nr, nc))
                    visit.add((nr, nc))
            length += 1
        
        return length if hasReachedEnd else -1