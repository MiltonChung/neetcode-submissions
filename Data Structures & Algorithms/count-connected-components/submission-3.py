class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = {}
        rank = {}

        for i in range(n):
            par[i] = i
            rank[i] = 0
        
        def find(n):
            while n != par[n]:
                par[n] = par[par[n]]
                n = par[n]
            return n
            
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
            elif rank[p1] < rank[p2]:
                par[p1] = p2
            else:
                par[p2] = p1
                rank[p1] += 1
            
            return True

        for e in edges:
            union(e[0], e[1])

        res = 0
        for k, v in par.items():
            if k == v:
                res += 1
            
        return res