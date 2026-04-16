class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString = ' '.join(char for char in s if char.isalnum()).lower()

        L, R = 0, len(newString) - 1
        while L < R:
            if newString[L] == newString[R]:
                L += 1
                R -= 1
            else:
                return False
        
        return True
