class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixSums = [0] * len(nums)
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            self.prefixSums[i] = total

    def sumRange(self, left: int, right: int) -> int:
        rightNum = self.prefixSums[right]
        if left > 0:
            leftNum = self.prefixSums[left - 1]
        else:
            leftNum = 0
        return rightNum - leftNum
