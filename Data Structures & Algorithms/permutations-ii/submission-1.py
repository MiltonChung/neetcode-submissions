class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(i):
            if i == len(nums):
                return [[]]
            
            res = []
            perms = backtrack(i + 1)
            for p in perms:
                for j in range(len(p) + 1):
                    pCopy = p.copy()
                    pCopy.insert(j, nums[i])
                    if pCopy not in res:
                        res.append(pCopy)

            return res

        nums.sort()
        return backtrack(0)