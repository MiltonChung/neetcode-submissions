class Solution:
    def longestPalindrome(self, s: str) -> str:
        substring = ''

        for i in range(len(s)):
            L, R = i, i
            while L >= 0 and R < len(s) and s[L] == s[R]:
                windowSize = R - L + 1
                if windowSize > len(substring):
                    substring = s[L:R + 1]
                L -= 1
                R += 1
            
            L, R = i, i + 1
            while L >= 0 and R < len(s) and s[L] == s[R]:
                windowSize = R - L + 1
                if windowSize > len(substring):
                    substring = s[L:R + 1]
                L -= 1
                R += 1

        return substring
