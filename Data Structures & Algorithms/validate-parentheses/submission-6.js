class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        const stack = [];
        const mapping = {
            ")": "(",
            "]": "[",
            "}": "{",
        };

        for (let char of s) {
            if (mapping[char] === undefined) {
                stack.push(char);
            } else {
                const popped = stack.pop();
                if (popped !== mapping[char]) {
                    return false;
                }
            }
        }

        return stack.length === 0;
    }
}
