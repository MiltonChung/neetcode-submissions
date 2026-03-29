class Solution:
    def climbStairs(self, n: int) -> int:
        def stairs(n, cache):
            if n == 0:
                return 1
            if n < 0:
                return 0

            if n in cache:
                return cache[n]
            
            cache[n] = stairs(n - 1, cache) + stairs(n - 2, cache)
            return cache[n]

        return stairs(n, {})