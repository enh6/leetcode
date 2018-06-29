class Solution {
public:
    bool exist(vector<vector<char>>& board, int x, int y, string& word, int i) {
        if (i == word.length()) {
            return true;
        }
        if (x < 0 || x >= board.size() || y < 0 || y >= board[0].size()) {
            return false;
        }
        if (board[x][y] != word[i]) {
            return false;
        }
        char c = board[x][y];
        board[x][y] = 0;
        bool exists =  exist(board, x + 1, y, word, i + 1) ||
            exist(board, x, y + 1, word, i + 1) ||
            exist(board, x - 1, y, word, i + 1) ||
            exist(board, x, y - 1, word, i + 1);
        board[x][y] = c;
        return exists;
    }
    bool exist(vector<vector<char>>& board, string word) {
        for (int x = 0; x < board.size(); x++) {
            for (int y = 0; y < board[0].size(); y++) {
                if (exist(board, x, y, word, 0)) {
                    return true;
                }
            }
        }
        return false;
    }
};