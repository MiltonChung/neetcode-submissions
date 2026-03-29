class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = [[-1] * len(word2) for _ in range(len(word1))]

        def dfs(i, j):
            if i == len(word1):
                return len(word2) - j
            elif j == len(word2):
                return len(word1) - i

            if memo[i][j] != -1:
                return memo[i][j]
            
            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1)
            else:
                return 1 + min(
                    dfs(i + 1, j),
                    dfs(i, j + 1),
                    dfs(i + 1, j + 1)
                )

        return dfs(0, 0)