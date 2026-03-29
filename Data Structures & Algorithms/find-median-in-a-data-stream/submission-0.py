class MedianFinder:
    def __init__(self):
        # small is max heap
        # large is min heap
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        # push to small(max heap). If the num is greater than the smallest num in large heap, put the num in large(min heap)
        heapq.heappush(self.small, -1 * num)
        if (self.small and self.large and (self.small[0] * -1) > self.large[0]):
            val = heapq.heappop(self.small) * -1
            heapq.heappush(self.large, val)

        # If the lengths are uneven(aka more than 1 difference in length)
        # swap the [0] position into the shorter length one
        if len(self.small) > len(self.large) + 1:
            val = heapq.heappop(self.small)
            heapq.heappush(self.large, val * -1)
        if len(self.small) + 1 < len(self.large):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, val * -1)

    def findMedian(self) -> float:
        # If the lengths are odd, return the [0] index of the longer one
        if len(self.small) > len(self.large):
            return self.small[0] * -1
        elif len(self.small) < len(self.large):
            return self.large[0]
        
        # If they're odd, return both [0] index and div by 2
        return ((self.small[0] * -1) + self.large[0]) / 2
