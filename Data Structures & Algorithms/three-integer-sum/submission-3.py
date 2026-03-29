class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            num = nums[i]
            # if num > 0: break
            if i > 0 and num == nums[i-1]: continue

            L, R = i + 1, len(nums) - 1
            while L < R:
                total = num + nums[L] + nums[R]
                if total > 0:
                    R -= 1
                elif total < 0:
                    L += 1
                else:
                    res.append([num, nums[L], nums[R]])
                    L += 1
                    while L < R and nums[L] == nums[L-1]:
                        L += 1
        
        return res