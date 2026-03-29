class Solution:
    def jump(self, nums: List[int]) -> int:
        dist = [0] * len(nums)
        minDist = float('inf')

        for i in range(len(nums) - 2, -1, -1):
            for j in range(i + 1, min(i + nums[i] + 1, len(nums))):
                if j == len(nums) - 1:
                    minDist = min(minDist, 1)
                else:
                    minDist = min(minDist, dist[j] + 1)
            dist[i] = minDist
            minDist = float('inf')

        return dist[0]
