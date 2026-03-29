class Solution:
    def reverseBits(self, n: int) -> int:
        bits = 31
        res = 0

        for i in range(bits, -1, -1):
            if n & 1 == 1:
                res = res + 2 ** bits
            n = n >> 1
            bits = bits - 1
        
        return res