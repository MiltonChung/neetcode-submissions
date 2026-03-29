class Solution:
    def climbStairs(self, n: int) -> int:
        def stairs(i, cache):
            if i >= n:
                return i == n

            if i in cache:
                return cache[i]
            
            cache[i] = stairs(i + 1, cache) + stairs(i + 2, cache)
            return cache[i]

        return stairs(0, {})
