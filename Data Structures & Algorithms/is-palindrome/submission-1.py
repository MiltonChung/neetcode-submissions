class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=''.join(char for char in s if char.isalnum()).lower()
        L, R = 0, len(s) - 1
        print(s)

        while L < R:
            if s[L] == s[R]:
                L += 1
                R -= 1
            else:
                return False
        
        return True