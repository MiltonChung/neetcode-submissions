class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        differenceSet = {}

        for index, num in enumerate(nums):
            diff = target - num

            if diff not in differenceSet:
                differenceSet[num] = index
            else:
                return [differenceSet[diff], index]