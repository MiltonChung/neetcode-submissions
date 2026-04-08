class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}

        for char in s:
            if char not in count:
                count[char] = 0
            count[char] += 1
        
        for i, c in enumerate(s):
            if count[c] == 1:
                return i

        return -1