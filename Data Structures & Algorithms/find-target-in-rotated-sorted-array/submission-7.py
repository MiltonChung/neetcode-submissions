class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1

        while L <= R:
            M = (R + L) // 2
            if nums[L] == target:
                return L
            if nums[R] == target:
                return R
            if nums[M] == target:
                return M
            if nums[M] > nums[R] and (target <= nums[R] or target > nums[M]):
                L = M + 1
            else:
                R = M - 1
        
        return -1