class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        sortedNums = sorted(nums)
        prevNum = 0

        for n in sortedNums:
            if prevNum == n:
                return n
            else:
                prevNum = n