class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        for i in range(len(s)):
            L, R = i, i
            while L >= 0 and R < len(s) and s[L] == s[R]:
                count += 1
                L -= 1
                R += 1
            
            L, R = i, i + 1
            while L >= 0 and R < len(s) and s[L] == s[R]:
                count += 1
                L -= 1
                R += 1
            
        return count