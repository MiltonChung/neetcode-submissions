/**
 * Forward declaration of guess API.
 * @param {number} num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * function guess(num) {}
 */

class Solution {
    /**
     * @param {number} n
     * @return {number}
     */
    guessNumber(n) {
        let low = 1
        let high = n

        while (low <= high) {
            const myGuess = Math.floor((low + high) / 2)

            if (guess(myGuess) < 0) {
                high = myGuess - 1
            } else if (guess(myGuess) > 0) {
                low = myGuess + 1
            } else {
                return myGuess
            }
        }
    }
}
