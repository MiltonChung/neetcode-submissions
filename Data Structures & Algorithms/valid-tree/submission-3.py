class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        adjList = {i: [] for i in range(n)}
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        visit = set()

        def dfs(node):
            if node in visit:
                return False
            
            visit.add(node)
            for nei in adjList[node]:
                if nei not in visit:
                    dfs(nei)
            return True
        
        return dfs(0) and len(visit) == n