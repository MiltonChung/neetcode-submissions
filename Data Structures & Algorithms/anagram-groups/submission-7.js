class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const hashmap = new Map();

        for (let w of strs) {
            const sortedWord = w.split("").sort().join("");
            if (!hashmap.has(sortedWord)) {
                hashmap.set(sortedWord, []);
            }
            hashmap.get(sortedWord).push(w);
        }

        return [...hashmap.values()];
    }
}
