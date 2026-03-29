class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for n in nums:
            curPerm = []
            for p in res:
                for j in range(len(p) + 1):
                    pCopy = p.copy()
                    pCopy.insert(j, n)
                    if pCopy not in curPerm:
                        curPerm.append(pCopy)
            res = curPerm
        return res
