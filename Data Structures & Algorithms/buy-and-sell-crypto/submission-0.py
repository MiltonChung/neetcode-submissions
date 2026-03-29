class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2: return 0

        profit = 0
        currMin = prices[0]
        
        for i in range(1, len(prices)):
            if prices[i] - currMin > profit:
                profit = prices[i] - currMin
            else:
                currMin = min(currMin, prices[i])
        
        return profit