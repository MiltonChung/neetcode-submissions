class Solution {
    /**
     * @param {character[][]} board
     * @param {string} word
     * @return {boolean}
     */
    exist(board, word) {
        const ROW = board.length
        const COL = board[0].length
        const visited = new Set()

        const dfs = (i, j, c) => {
            if (c === word.length) return true
            if (i === ROW || j === COL || i < 0 || j < 0) return false
            if (board[i][j] !== word[c]) return false
            if (visited.has(`${i},${j}`)) return false

            visited.add(`${i},${j}`)
            const res = (
                dfs(i - 1, j, c + 1) ||
                dfs(i, j + 1, c + 1) ||
                dfs(i + 1, j, c + 1) ||
                dfs(i, j - 1, c + 1)
            )
            visited.delete(`${i},${j}`)
            return res
        }

        for (let i=0; i<ROW; i++) {
            for (let j=0; j<COL; j++) {
                if (board[i][j] === word[0]) {
                    if (dfs(i, j, 0)) return true
                }
            }
        }

        return false
    }
}
