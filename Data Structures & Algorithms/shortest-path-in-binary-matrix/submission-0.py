class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        queue = deque()
        visit.add((0, 0))
        queue.append((0, 0))

        length = 1
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if grid[r][c] == 1:
                    return -1
                if r == ROWS - 1 and c == COLS - 1:
                    return length
                
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
                for dr, dc in directions:
                    newR, newC = r + dr, c + dc
                    if (min(newR, newC) < 0 or
                        newR == ROWS or newC == COLS or
                        (newR, newC) in visit or
                        grid[newR][newC] == 1):
                        continue
                    queue.append((newR, newC))
                    visit.add((newR, newC))
            length += 1
        return -1