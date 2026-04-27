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
        if (pairs.length === 0) return pairs;
        return this.mergeSortHelper(pairs, 0, pairs.length - 1)
    }

    mergeSortHelper(arr, l, r) {
        if (l < r) {
            let m = Math.floor((l + r) / 2)

            this.mergeSortHelper(arr, l, m)
            this.mergeSortHelper(arr, m + 1, r)
            this.merge(arr, l, m, r)
        }

        return arr
    }

    merge(arr, l, m, r) {
        const length1 = m - l + 1
        const length2 = r - m

        const L = arr.slice(l, m + 1);
        const R = arr.slice(m + 1, r + 1);
        let i = 0, j = 0, k = l

        while (i < length1 && j < length2) {
            if (L[i].key <= R[j].key) {
                arr[k] = L[i]
                i++
            } else {
                arr[k] = R[j]
                j++
            }
            k++
        }

        while (i < length1) {
            arr[k] = L[i]
            i++
            k++
        }

        while (j < length2) {
            arr[k] = R[j]
            j++
            k++
        }
    }
}