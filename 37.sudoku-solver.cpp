class Solution {
public:
    bool solve(vector<vector<char>>& board, array<array<array<bool, 9>, 9>, 3>& state, int i_begin, int j_begin) {
        for (int i = i_begin; i < 9; i++) {
            for (int j = j_begin; j < 9; j++) {
                if (board[i][j] == '.') {
                    for (int n = 0; n < 9; n++) {
                        if(state[0][i][n] == false && state[1][j][n] == false && state[2][j / 3 * 3 + i / 3][n] == false) {
                            board[i][j] = '1' + n;
                            state[0][i][n] = true;
                            state[1][j][n] = true;
                            state[2][j / 3 * 3 + i / 3][n] = true;
                            if (solve(board, state, i_begin, j_begin)) {
                                return true;
                            }
                            state[0][i][n] = false;
                            state[1][j][n] = false;
                            state[2][j / 3 * 3 + i / 3][n] = false;
                        }
                    }
                    board[i][j] = '.';
                    return false;
                }
            }
        }
        return true;
    }

    void solveSudoku(vector<vector<char>>& board) {
        array<array<array<bool, 9>, 9>, 3> state;
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                state[0][i][j] = false;
                state[1][i][j] = false;
                state[2][i][j] = false;
            }
        }
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] != '.') {
                    int pos = board[i][j] - '1';
                    state[0][i][pos] = true;
                    state[1][j][pos] = true;
                    state[2][j / 3 * 3 + i / 3][pos] = true;
                }
            }
        }
        solve(board, state, 0, 0);
    }
};