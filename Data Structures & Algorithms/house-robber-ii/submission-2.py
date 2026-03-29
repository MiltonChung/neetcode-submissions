class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def dfs(i, cache):
            if i >= len(nums):
                return 0
            if i in cache:
                return cache[i]
            
            cache[i] = max(nums[i] + dfs(i+2, cache), dfs(i+1, cache))
            return cache[i]

        def dfs2(i, cache):
            if i >= len(nums) - 1:
                return 0
            if i in cache:
                return cache[i]
            
            cache[i] = max(nums[i] + dfs2(i+2, cache), dfs2(i+1, cache))
            return cache[i]

        return max(dfs(1, {}), dfs2(0, {}))