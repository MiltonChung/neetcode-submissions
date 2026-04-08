class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        if len(nums) == 1: return nums
        L, R = 0, 1

        while R < len(nums):
            if nums[R] == 0:
                R += 1
                continue
            if nums[L] != 0:
                L += 1
                if L == R: R += 1
                continue
            if nums[R] != 0 and nums[L] == 0:
                nums[R], nums[L] = nums[L], nums[R]
