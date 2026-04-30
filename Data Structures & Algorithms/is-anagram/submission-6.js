class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        const hashmap = new Map();

        for (let i = 0; i < s.length; i++) {
            hashmap.set(s[i], (hashmap.get(s[i]) || 0) + 1);
        }

        for (let j = 0; j < t.length; j++) {
            const letter = hashmap.get(t[j]);
            if (letter == null || letter === 0) return false;
            hashmap.set(t[j], letter - 1);
        }

        return hashmap.values().every((num) => num === 0);
    }
}
