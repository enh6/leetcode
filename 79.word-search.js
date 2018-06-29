/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */
var exist = function(board, word) {
    let exist_helper = function(x, y, i) {
        if (i == word.length) {
            return true;
        }
        if (x < 0 || x >= board.length || y < 0 || y >= board[0].length) {
            return false;
        }
        if (board[x][y] != word[i]) {
            return false;
        }
        let c = board[x][y];
        board[x][y] = 0;
        let exists =  exist_helper(x + 1, y, i + 1) ||
            exist_helper(x, y + 1, i + 1) ||
            exist_helper(x - 1, y, i + 1) ||
            exist_helper(x, y - 1, i + 1);
        board[x][y] = c;
        return exists;
    }
    for (let x = 0; x < board.length; x++) {
        for (let y = 0; y < board[0].length; y++) {
            if (exist_helper(x, y, 0)) {
                return true;
            }
        }
    }
    return false;
};