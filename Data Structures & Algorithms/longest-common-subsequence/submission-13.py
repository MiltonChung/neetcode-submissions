class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        memo = [[0] * (n + 1) for _ in range(m + 1)]

        for t1 in range(m):
            for t2 in range(n):
                if text1[t1] == text2[t2]:
                    memo[t1+1][t2+1] = memo[t1][t2] + 1
                else:
                    memo[t1+1][t2+1] = max(
                        memo[t1 + 1][t2],
                        memo[t1][t2 + 1]
                    )

        return memo[m][n]