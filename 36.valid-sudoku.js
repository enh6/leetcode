/**
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = function(board) {
    for (let i = 0; i < 9; i++) {
        let pos_array = [];
        for (let j = 0; j < 9; j++) {
            if (board[i][j] != '.') {
                let pos = board[i][j] - '1';
                if (pos_array[pos]) {
                    return false;
                } else {
                    pos_array[pos] = true;
                }
            }
        }
    }
    for (let i = 0; i < 9; i++) {
        let pos_array = [];
        for (let j = 0; j < 9; j++) {
            if (board[j][i] != '.') {
                let pos = board[j][i] - '1';
                if (pos_array[pos]) {
                    return false;
                } else {
                    pos_array[pos] = true;
                }
            }
        }
    }
    for (let i = 0; i < 9; i++) {
        let pos_array = [];
        for (let j = 0; j < 9; j++) {
            if (board[Math.floor(i / 3) * 3 + Math.floor(j / 3)][i % 3 * 3 + j % 3] != '.') {
                let pos = board[Math.floor(i / 3) * 3 + Math.floor(j / 3)][i % 3 * 3 + j % 3] - '1';
                if (pos_array[pos]) {
                    return false;
                } else {
                    pos_array[pos] = true;
                }
            }
        }
    }
    return true;
};