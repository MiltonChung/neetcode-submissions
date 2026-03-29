class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftRight, rightLeft = [0] * len(nums), [0] * len(nums)
        res = []

        prefix = 1
        for i in range(len(nums)):
            if i - 1 < 0:
                leftRight[i] = prefix
            else:
                prefix *= nums[i - 1]
                leftRight[i] = prefix
        
        prefix = 1
        for j in range(len(nums) - 1, -1, -1):
            if j == len(nums) - 1:
                rightLeft[j] = prefix
            else:
                prefix *= nums[j + 1]
                rightLeft[j] = prefix

        for k in range(len(leftRight)):
            res.append(leftRight[k] * rightLeft[k])

        return res