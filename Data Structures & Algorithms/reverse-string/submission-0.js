class Solution {
    /**
     * @param {character[]} s
     * @return {void} Do not return anything, modify s in-place instead.
     */
    reverseString(s) {
        let L = 0;
        let R = s.length - 1;

        while (L <= R) {
            if (s[R] !== s[L]) {
                const temp = s[R];
                s[R] = s[L];
                s[L] = temp;
            }
            L++;
            R--;
        }
    }
}
