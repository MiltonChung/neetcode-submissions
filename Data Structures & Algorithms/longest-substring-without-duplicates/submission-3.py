class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        L, maxSize = 0, 0

        for R in range(len(s)):
            while s[R] in window:
                window.remove(s[L])
                L += 1
            window.add(s[R])
            maxSize = max(maxSize, R - L + 1)

        return maxSize
        