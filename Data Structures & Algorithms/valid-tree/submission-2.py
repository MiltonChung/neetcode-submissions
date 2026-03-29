class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = {i: [] for i in range(n)}
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        visit = set()

        def dfs(node, prev):
            if node in visit:
                return False
            
            visit.add(node)
            for nei in adjList[node]:
                if nei == prev: continue
                if not dfs(nei, node):
                        return False
            return True

        return dfs(0, -1) and len(visit) == n
