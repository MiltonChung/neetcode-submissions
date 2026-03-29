class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        res = []

        def dfs(i, j, island, prev):
            if i < 0 or i >= ROWS or j < 0 or j >= COLS:
                return
            if (i, j) in island:
                return
            if prev > heights[i][j]:
                return

            island.add((i, j))
            dfs(i - 1, j, island, heights[i][j])
            dfs(i, j - 1, island, heights[i][j])
            dfs(i + 1, j, island, heights[i][j])
            dfs(i, j + 1, island, heights[i][j])

        for i in range(ROWS):
            dfs(i, 0, pacific, heights[i][0])
            dfs(i, COLS - 1, atlantic, heights[i][COLS - 1])
        
        for j in range(COLS):
            dfs(0, j, pacific, heights[0][j])
            dfs(ROWS - 1, j, atlantic, heights[ROWS - 1][j])

        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) in pacific and (i, j) in atlantic:
                    res.append([i, j])

        return res