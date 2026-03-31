class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = " ".join(char for char in s if char.isalnum()).lower()
        L, R = 0, len(newS) - 1

        while L < R:
            if newS[L] == newS[R]:
                L += 1
                R -= 1
            else:
                return False
        
        return True