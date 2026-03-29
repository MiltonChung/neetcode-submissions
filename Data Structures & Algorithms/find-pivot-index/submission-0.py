class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftPrefixSum, rightPrefixSum = [0] * len(nums), [0] * len(nums)
        
        prefix = 0
        for i in range(len(nums)):
            prefix += nums[i]
            leftPrefixSum[i] = prefix
        
        prefix = 0
        for i in range(len(nums) - 1, -1, -1):
            prefix += nums[i]
            rightPrefixSum[i] = prefix
        
        for i in range(len(nums)):
            if leftPrefixSum[i] == rightPrefixSum[i]:
                return i
        
        return -1