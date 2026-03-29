class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        gMax = gMin = nums[0]
        curMax, curMin = 0, 0
        total = 0

        for n in nums:
            total += n
            curMin = min(n, curMin + n)
            curMax = max(n, curMax + n)
            gMin = min(curMin, gMin)
            gMax = max(curMax, gMax)

        if gMax > 0:
            return max(gMax, total - gMin)
        else:
            return gMax