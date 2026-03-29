class Solution:
    def jump(self, nums: List[int]) -> int:
        dist = [float('inf')] * len(nums)
        dist[-1] = 0

        for i in range(len(nums) - 2, -1, -1):
            for j in range(i + 1, min(i + nums[i] + 1, len(nums))):
                dist[i] = min(dist[i], dist[j] + 1)

        return dist[0]
