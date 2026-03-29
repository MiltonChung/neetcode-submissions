class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        target = threshold * k
        window_sum = sum(arr[:k])
        count = 1 if window_sum >= target else 0

        for r in range(k, len(arr)):
            window_sum += arr[r] - arr[r - k]
            if window_sum >= target:
                count += 1

        return count
