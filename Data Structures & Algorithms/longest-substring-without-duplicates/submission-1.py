class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxSize, curSize = 0, 0
        window = set()
        L = 0

        for R in range(len(s)):
            curSize += 1
            if s[R] in window:
                while s[L] != s[R]:
                    window.remove(s[L])
                    L += 1
                    curSize -= 1
                L += 1
                if s[L] == s[R]:
                    curSize = 1
                else:
                    curSize -= 1
            else:
                window.add(s[R])
            maxSize = max(curSize, maxSize)
        
        return maxSize