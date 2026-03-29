class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)
        target = length - 1
        
        for i in range(length - 2, -1, -1):
            if nums[i] + i < target:
                continue
            target = i
        
        return target == 0