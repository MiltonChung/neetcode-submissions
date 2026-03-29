class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        for b in s:
            if len(stack) == 0 and b not in mapping:
                return False
            if b in mapping:
                stack.append(b)
            else:
                popped = stack.pop()
                if mapping[popped] != b:
                    return False
        
        return len(stack) == 0