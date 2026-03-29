/** Pair class to store key-value pairs */
// class Pair {
//   /**
//    * @param {number} key The key to be stored in the pair
//    * @param {string} value The value to be stored in the pair
//    */
//   constructor(key, value) {
//       this.key = key;
//       this.value = value;
//   }
// }
class Solution {
    /**
     * @param {Pair[]} pairs
     * @returns {Pair[]}
     */
    quickSort(pairs) {
        return this.sort(pairs, 0, pairs.length - 1)
    }

    sort(pairs, start, end) {
        if (end - start + 1 <= 1) return pairs

        let pivot = end
        let left = start

        for (let i = start; i < end; i++) {
            if (pairs[pivot].key > pairs[i].key) {
                let temp = pairs[left]
                pairs[left] = pairs[i]
                pairs[i] = temp
                left++
            }
        }

        let temp = pairs[left]
        pairs[left] = pairs[pivot]
        pairs[pivot] = temp

        this.sort(pairs, start, left - 1)
        this.sort(pairs, left + 1, end)

        return pairs













        // if (end - start + 1 <= 1) {
        //     return pairs
        // }

        // let pivot = end
        // let left = start

        // for (let i = start; i < end; i++) {
        //     if (pairs[pivot].key > pairs[i].key) {
        //         const temp = pairs[i]
        //         pairs[i] = pairs[left]
        //         pairs[left] = temp
        //         left++
        //     }
        // }

        // const temp = pairs[left]
        // pairs[left] = pairs[pivot]
        // pairs[pivot] = temp

        // this.sort(pairs, start, left - 1)
        // this.sort(pairs, left + 1, end)

        // return pairs
    }
}
