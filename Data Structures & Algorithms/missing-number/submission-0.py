class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        target = 0
        for i in range(len(nums) + 1):
            target += i
        
        current = 0
        for n in nums:
            current += n
        
        return target - current