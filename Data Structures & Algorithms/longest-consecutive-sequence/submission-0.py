class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)
        sequenceStart = []
        res = 0

        for n in setNums:
            if n - 1 not in setNums:
                sequenceStart.append(n)

        for n in sequenceStart:
            start = n
            count = 1
            while (start + 1) in setNums:
                count += 1
                start += 1
            res = max(res, count)
        
        return res
