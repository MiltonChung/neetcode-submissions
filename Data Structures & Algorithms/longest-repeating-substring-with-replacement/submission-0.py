class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res, L = 0, 0
        charTable = {}

        for R in range(len(s)):
            charTable[s[R]] = charTable.get(s[R], 0) + 1

            while (R - L + 1) - max(charTable.values()) > k:
                charTable[s[L]] -= 1
                L += 1
            
            res = max(res, R - L + 1)

        return res