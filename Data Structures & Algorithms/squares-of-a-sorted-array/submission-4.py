class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        neg, pos, res = [], [], []

        for i in range(len(nums)):
            if nums[i] < 0:
                neg.append(nums[i] * nums[i])
            else:
                pos.append(nums[i] * nums[i])

        neg.reverse()
        i = j = 0
        while i < len(neg) or j < len(pos):
            val1 = neg[i] if i < len(neg) else float('inf')
            val2 = pos[j] if j < len(pos) else float('inf')

            if val1 < val2:
                res.append(val1)
                i += 1
            else:
                res.append(val2)
                j += 1
        
        return res