class Solution {
    /**
     * @param {number[]} piles
     * @param {number} h
     * @return {number}
     */
    minEatingSpeed(piles, h) {
        let high = Math.max(...piles)
        let low = 1

        while (low < high) {
            const mid = low + Math.floor((high - low) / 2)

            if (this.canFinish(mid, h, piles)) {
                high = mid
            } else {
                low = mid + 1
            }
        }

        return low
    }

    canFinish(mid, h, piles) {
        let i = 0
        let tempPiles = [...piles]

        while (i < tempPiles.length) {
            let res = Math.floor(tempPiles[i] / mid)
            if ((tempPiles[i] % mid) > 0) res++
            tempPiles[i] = res
            i++
        }

        let res = 0
        for (let num of tempPiles) {
            res = res + num
        }

        if (res <= h) return true
        else return false
    }
}
