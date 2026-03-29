class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        n = len(intervals)

        # add all intervals that appear before newInterval[0]
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        # merge any overlapping intervals
        while i < n and intervals[i][0] <= newInterval[1]:
            minNum = min(newInterval[0], intervals[i][0])
            maxNum = max(newInterval[1], intervals[i][1])
            newInterval = [minNum, maxNum]
            i += 1
        res.append(newInterval)

        # add the remaining intervals
        while i < n:
            res.append(intervals[i])
            i += 1

        return res