class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        s1, s2 = len(s), len(t)
        memo = [[-1] * s2 for _ in range(s1)]
        
        def dfs(i, j):
            if j == s2:
                return 1
            if i == s1:
                return 0
            
            if memo[i][j] != -1:
                return memo[i][j]
            
            include = 0
            if s[i] == t[j]:
                include = dfs(i + 1, j + 1)
            skip = dfs(i + 1, j)

            memo[i][j] = include + skip
            return memo[i][j]
        
        return dfs(0, 0)