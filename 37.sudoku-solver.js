/**
 * @param {character[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
var solveSudoku = function(board) {
    var solve = function(board, state, i_begin, j_begin) {
        for (let i = i_begin; i < 9; i++) {
            for (let j = j_begin; j < 9; j++) {
                if (board[i][j] == '.') {
                    let pos = Math.floor(j / 3) * 3 + Math.floor(i / 3);
                    for (let n = 0; n < 9; n++) {
                        if(state[0][i][n] == false && state[1][j][n] == false && state[2][pos][n] == false) {
                            board[i][j] = (1 + n).toString();
                            state[0][i][n] = true;
                            state[1][j][n] = true;
                            state[2][pos][n] = true;
                            if (solve(board, state, i_begin, j_begin)) {
                                return true;
                            }
                            state[0][i][n] = false;
                            state[1][j][n] = false;
                            state[2][pos][n] = false;
                        }
                    }
                    board[i][j] = '.';
                    return false;
                }
            }
        }
        return true;
    };

    let state = [[], [], []];
    for (let i = 0; i < 9; i++) {
        state[0][i] = new Array();
        state[1][i] = new Array();
        state[2][i] = new Array();
        for (let j = 0; j < 9; j++) {
            state[0][i][j] = false;
            state[1][i][j] = false;
            state[2][i][j] = false;
        }
    }
    for (let i = 0; i < 9; i++) {
        for (let j = 0; j < 9; j++) {
            if (board[i][j] != '.') {
                let pos = board[i][j] - '1';
                state[0][i][pos] = true;
                state[1][j][pos] = true;
                state[2][Math.floor(j / 3) * 3 + Math.floor(i / 3)][pos] = true;
            }
        }
    }
    solve(board, state, 0, 0);
};