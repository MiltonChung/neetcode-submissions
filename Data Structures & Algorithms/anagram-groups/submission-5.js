class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const map = new Map()

        for (let i=0; i<strs.length; i++) {
            const word = strs[i]
            const sortedWord = word.split('').sort().join('')

            if (!map.has(sortedWord)) {
                map.set(sortedWord, [])
            }
            map.get(sortedWord).push(word)
        }

        const res = []
        for (let [key, value] of map) {
            res.push(value)
        }
        return res
    }
}
