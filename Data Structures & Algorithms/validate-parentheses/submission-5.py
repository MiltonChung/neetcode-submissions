class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            "(": ')',
            "{": "}",
            "[": "]"
        }

        for char in s:
            if char in mapping:
                stack.append(mapping[char])
                continue
            elif len(stack) > 0:
                popped = stack.pop()
                if char != popped:
                    return False
            else:
                return False
        
        return True if len(stack) == 0 else False