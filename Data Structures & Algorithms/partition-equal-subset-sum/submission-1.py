class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        if totalSum % 2 != 0: return False
        target = totalSum // 2
        memo = {}

        def dfs(i, curSum):
            if curSum == target:
                return True
            if i >= len(nums):
                return False
            
            key = (i, curSum)
            if key in memo:
                return memo[key]

            memo[key] = dfs(i + 1, curSum) or dfs(i + 1, curSum + nums[i])
            return memo[key]

        return dfs(0, 0)