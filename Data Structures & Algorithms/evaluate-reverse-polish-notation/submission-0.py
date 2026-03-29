class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1: return int(tokens[0])
        stack = []

        for t in tokens:
            if t == '+':
                second, first = stack.pop(), stack.pop()
                res = first + second
                stack.append(res)
                continue
            
            if t == '-':
                second, first = stack.pop(), stack.pop()
                res = first - second
                stack.append(res)
                continue

            if t == '*':
                second, first = stack.pop(), stack.pop()
                res = first * second
                stack.append(res)
                continue

            if t == '/':
                second, first = stack.pop(), stack.pop()
                res = int(first / second)
                stack.append(res)
                continue

            stack.append(int(t))

        return stack.pop()