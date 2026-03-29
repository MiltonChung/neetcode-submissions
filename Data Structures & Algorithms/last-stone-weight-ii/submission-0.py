class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = total // 2
        memo = {}

        def dfs(i, curSum):
            if curSum >= target or i == len(stones):
                return abs(curSum - (total-curSum))
            key = (i, curSum)
            if key in memo:
                return memo[key]
            
            memo[key] = min(dfs(i + 1, curSum), dfs(i + 1, curSum + stones[i]))
            return memo[key]

        return dfs(0, 0)