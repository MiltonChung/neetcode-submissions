class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        n = len(intervals)

        # merge before overlapping
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        # find overlapping intervals
        while i < n and intervals[i][0] <= newInterval[1]:
            minNum = min(intervals[i][0], newInterval[0])
            maxNum = max(intervals[i][1], newInterval[1])
            newInterval = [minNum, maxNum]
            i += 1
        res.append(newInterval)

        # merge after overlapping
        while i < n:
            res.append(intervals[i])
            i += 1

        return res