class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob(i, cache):
            if i >= len(nums):
                return 0
            if i in cache:
                return cache[i]
            
            cache[i] = max(nums[i] + rob(i+2, cache), rob(i+1, cache))
            return cache[i]
        
        return rob(0, {})