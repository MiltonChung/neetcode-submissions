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
    mergeSort(pairs) {
        return this.mergeSortHelper(pairs, 0, pairs.length - 1)
    }

    mergeSortHelper(pairs, left, right) {
        if (left < right) {
            const middle = Math.floor((left + right) / 2)

            this.mergeSortHelper(pairs, left, middle)
            this.mergeSortHelper(pairs, middle + 1, right)
            this.merge(pairs, left, middle, right)
        }

        return pairs
    }

    merge(pairs, left, middle, right) {
        const length1 = middle - left + 1
        const length2 = right - middle

        let leftSubArr = new Array(length1)
        let rightSubArr = new Array(length2)

        for (let i = 0; i < length1; i++) {
            leftSubArr[i] = pairs[left + i]
        }

        for (let j = 0; j < length2; j++) {
            rightSubArr[j] = pairs[middle + 1 + j]
        }

        let i = 0
        let j = 0
        let k = left

        while (i < length1 && j < length2) {
            if (leftSubArr[i].key <= rightSubArr[j].key) {
                pairs[k] = leftSubArr[i]
                i++
            } else {
                pairs[k] = rightSubArr[j]
                j++
            }
            k++
        }

        while (i < length1) {
            pairs[k] = leftSubArr[i]
            i++
            k++
        }

        while (j < length2) {
            pairs[k] = rightSubArr[j]
            j++
            k++
        }
    }
}




