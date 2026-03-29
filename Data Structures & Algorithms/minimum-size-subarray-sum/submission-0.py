class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = len(nums) + 1
        curSum = L = 0

        for R in range(len(nums)):
            curSum += nums[R]
            while curSum >= target:
                res = min(res, R - L + 1)
                curSum -= nums[L]
                L += 1
        
        if res == len(nums) + 1:
            return 0
        else:
            return res