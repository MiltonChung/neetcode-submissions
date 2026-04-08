class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals

        # i = 0
        res = []
        intervals.sort(key=lambda i: i[0])

        for i in range(len(intervals)):
            if i + 1 < len(intervals) and intervals[i][1] >= intervals[i+1][0]:
                minNumber = min(intervals[i][0], intervals[i+1][0])
                maxNumber = max(intervals[i][1], intervals[i+1][1])
                intervals[i+1] = [minNumber, maxNumber]
            else:
                res.append(intervals[i])
 
        return res