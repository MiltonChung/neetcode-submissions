class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parents = [0] * n
        size = [0] * n
        components = n

        for i in range(n):
            parents[i] = i
            size[i] = 0
        
        def find(node):
            while node != parents[node]:
                parents[node] = parents[parents[node]]
                node = parents[node]
            return node
        
        def union(n1, n2):
            nonlocal components
            
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            
            components -= 1
            if size[p1] > size[p2]:
                parents[p2] = p1
                size[p1] += 1
            else:
                parents[p1] = p2
                size[p2] += 1
            return True

        for u, v in edges:
            if not union(u, v):
                # contains cycle
                return False
        
        # Ensures all nodes are connected
        return components == 1