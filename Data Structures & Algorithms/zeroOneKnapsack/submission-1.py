class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        memo = [[-1] * (capacity + 1) for _ in range(len(profit))]

        def dfs(i, cap):
            if i == len(profit):
                return 0
            if memo[i][cap] != -1:
                return memo[i][cap]

            #skip
            memo[i][cap] = dfs(i + 1, cap)

            #include
            curCap = cap - weight[i]
            if curCap >= 0:
                p = profit[i] + dfs(i + 1, curCap)
                memo[i][cap] = max(memo[i][cap], p)
            
            return memo[i][cap]

        return dfs(0, capacity)