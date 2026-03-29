class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0 for _ in range(n+1)]
        
        for i in range(n + 1):
            ans[i] = self.count(i)

        return ans
    
    def count(self, n):
        count = 0
        while n > 0:
            if n & 1 == 1:
                count += 1
            n = n >> 1
        
        return count