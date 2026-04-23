class Solution {
    /**
     * @param {number[][]} intervals
     * @return {number[][]}
     */
    merge(intervals) {
        intervals.sort((a, b) => a[0] - b[0])
        const res = [intervals[0]]

        for (let i=1; i<intervals.length; i++) {
            const resLastIndex = res.length -1
            if (intervals[i][0] <= res[resLastIndex][1]) {
                const newStart = Math.min(intervals[i][0], res[resLastIndex][0])
                const newEnd = Math.max(intervals[i][1], res[resLastIndex][1])
                res[resLastIndex] = [newStart, newEnd]
            } else {
                res.push(intervals[i])
            }
        }

        return res
    }
}
