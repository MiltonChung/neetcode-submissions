class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        if (s.length % 2 !== 0) return false
        let stack = []
        const brackets = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for (let i = 0; i < s.length; i++) {
            if (brackets[s[i]] !== undefined) {
                const lastItem = stack[stack.length - 1]
                if (brackets[s[i]] === lastItem) {
                    if (stack.length < 1) return false
                    stack.pop()
                } else {
                    return false
                }
            } else {
                stack.push(s[i])
            }
        }

        if (stack.length === 0) return true
        else return false
    }
}
