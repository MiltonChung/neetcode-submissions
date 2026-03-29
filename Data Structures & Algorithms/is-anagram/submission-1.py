class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False

        char = {}

        for i in s:
            char[i] = char.get(i, 0) + 1
        
        for j in t:
            if j not in char or char[j] == 0:
                return False
            char[j] -= 1
        
        for v in char.values():
            if v != 0:
                return False
        
        return True