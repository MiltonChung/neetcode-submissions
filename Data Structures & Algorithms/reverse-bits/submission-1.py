class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(31, -1, -1):
            if n & 1 == 1:
                res = res + 2 ** i
            n = n >> 1
        
        return res