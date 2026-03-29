class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = [[] for _ in range(n)]
        visited = [False] * n

        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        def dfs(n):
            for neighbor in adjList[n]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    dfs(neighbor)
        
        res = 0
        for n in range(n):
            if not visited[n]:
                visited[n] = True
                dfs(n)
                res += 1
        
        return res