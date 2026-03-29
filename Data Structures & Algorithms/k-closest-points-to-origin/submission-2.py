class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = []
        for point in points:
            calc = math.sqrt((point[0])**2 + (point[1])**2)
            distance.append((calc, point))

        heapq.heapify(distance)
        res = []

        while len(res) < k:
            shortest = heapq.heappop(distance)
            res.append(shortest[1])

        return res