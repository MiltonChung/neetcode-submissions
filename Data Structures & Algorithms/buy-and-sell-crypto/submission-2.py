class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1: return 0
        
        maxProfit = 0
        L, R = 0, 1

        while R < len(prices):
            if prices[L] >= prices[R]:
                L = R
            else:
                profit = prices[R] - prices[L]
                maxProfit = max(profit, maxProfit)
            R += 1

        return maxProfit