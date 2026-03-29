class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        curAvg = 0
        L = 0

        curAvg = sum(arr[:k]) / k
        if curAvg >= threshold:
            count += 1

        for R in range(k, len(arr)):
            if R - L + 1 > k:
                curAvg = (curAvg * k - arr[L] + arr[R]) / k
                L += 1
            if curAvg >= threshold:
                count += 1
        
        return count
            