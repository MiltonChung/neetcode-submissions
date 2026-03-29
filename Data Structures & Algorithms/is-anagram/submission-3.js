class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (s.length !== t.length) {
            return false
        }

        const counter = {}

        for (let i=0; i<s.length; i++) {
            counter[s[i]] = (counter[s[i]] || 0) + 1
        }
        
        for (let j=0; j<t.length; j++) {
            if (!counter[t[j]] || counter[t[j]] === 0) {
                return false
            }
            counter[t[j]] = (counter[t[j]] || 0) - 1
        }

        for (const key in counter) {
            if (counter[key] !== 0) return false
        }

        return true
    }
}
