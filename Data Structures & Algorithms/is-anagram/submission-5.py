class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        hashmap = {}

        for c in s:
            if c not in hashmap:
                hashmap[c] = 0
            hashmap[c] += 1
        
        for c in t:
            if c not in hashmap or hashmap[c] <= 0:
                return False
            hashmap[c] -= 1
        
        return True