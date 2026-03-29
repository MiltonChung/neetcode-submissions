class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        if totalSum % 2 != 0: return False

        def dfs(i, curSum):
            if i >= len(nums):
                return False
            
            # skip
            if dfs(i + 1, curSum):
                return True

            # include
            curSum += nums[i]
            if curSum < totalSum / 2:
                return dfs(i + 1, curSum)
            elif curSum == totalSum / 2:
                return True
            return False
        
        return dfs(0, 0)