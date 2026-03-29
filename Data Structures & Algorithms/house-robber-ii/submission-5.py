class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        def dfs(i, end_idx, cache):
            if i >= end_idx:
                return 0
            if i in cache:
                return cache[i]
            
            cache[i] = max(nums[i] + dfs(i + 2, end_idx, cache), dfs(i + 1, end_idx, cache))
            return cache[i]
        
        return max(dfs(0, len(nums) - 1, {}), dfs(1, len(nums), {}))