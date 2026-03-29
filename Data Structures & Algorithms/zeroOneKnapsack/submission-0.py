class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        maxProfit = 0

        def dfs(i, cap):
            if i == len(profit):
                return 0

            #skip
            maxProfit = dfs(i + 1, cap)

            #include
            curCap = cap - weight[i]
            if curCap >= 0:
                p = profit[i] + dfs(i + 1, curCap)
                maxProfit = max(maxProfit, p)
            
            return maxProfit

        
        return dfs(0, capacity)