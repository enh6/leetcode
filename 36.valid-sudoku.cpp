class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        for (int i = 0; i < 9; i++) {
            array<bool, 9> pos_array;
            pos_array.fill(false);
            for (int j = 0; j < 9; j++) {
                if (board[i][j] != '.') {
                    int pos = board[i][j] - '1';
                    if (pos_array[pos]) {
                        return false;
                    } else {
                        pos_array[pos] = true;
                    }
                }
            }
        }
        for (int i = 0; i < 9; i++) {
            array<bool, 9> pos_array;
            pos_array.fill(false);
            for (int j = 0; j < 9; j++) {
                if (board[j][i] != '.') {
                    int pos = board[j][i] - '1';
                    if (pos_array[pos]) {
                        return false;
                    } else {
                        pos_array[pos] = true;
                    }
                }
            }
        }
        for (int i = 0; i < 9; i++) {
            array<bool, 9> pos_array;
            pos_array.fill(false);
            for (int j = 0; j < 9; j++) {
                if (board[i / 3 * 3 + j / 3][i % 3 * 3 + j % 3] != '.') {
                    int pos = board[i / 3 * 3 + j / 3][i % 3 * 3 + j % 3] - '1';
                    if (pos_array[pos]) {
                        return false;
                    } else {
                        pos_array[pos] = true;
                    }
                }
            }
        }
        return true;
    }
};